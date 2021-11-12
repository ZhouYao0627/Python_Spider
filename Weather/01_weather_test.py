import io
import sys
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import pymysql

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码, 防止控制台打印乱码


# 获取数据
def get_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        # response.encoding = response.apparent_encoding
        response.encoding = 'gbk'
        return response.text  # 以字符串的形式来返回了网页的源码
    except requests.HTTPError:
        return 'requests.HTTPError'


# 解析数据
def parse_data(html):
    soup = BeautifulSoup(html, 'lxml')
    all_weather = soup.find('div', 'wdetail').find('table').find_all('tr')

    data = list()
    for tr in all_weather[2:]:
        td_list = tr.find_all('td')
        for td in td_list:
            s = td.get_text()
            data.append(''.join(s.split()))

    res = np.array(data).reshape(-1, 8)
    return res


# def saveTocsv(data, fileName):
#     # 城市  日期	天气状况	风力方向	最高温度	天气状况	风力方向	最低温度，用下面的数字分别代表
#     result_weather = pd.DataFrame(data, columns=['城市', '日期', '天气状况', '风力方向', '最高温度', '天气状况', '风力方向', '最低温度'])
#     result_weather.to_csv(fileName, index=False, encoding='gbk')
#     print('Save all weather success!')


def saveToMysql(data):
    conn = pymysql.connect(user='root', password='123456', host='localhost', database='weather1', port=3306,
                           charset='utf8')
    cursor = conn.cursor()

    sql = 'INSERT INTO weather(city,date1 ,con,wind,maxtemp,con1,wind1,mintemp) values (%s,%s,%s,%s,%s,%s,%s,%s)'
    data_list = np.ndarray.tolist(data)
    try:
        cursor.executemany(sql, data_list)
        print(cursor.rowcount)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


if __name__ == '__main__':
    url = 'http://www.tianqihoubao.com/weather/top/hefei.html'

    html = get_page(url)  # 获取数据
    data_p = parse_data(html)  # 解析数据

    # saveTocsv(data_p, "14.csv")
    saveToMysql(data_p)
