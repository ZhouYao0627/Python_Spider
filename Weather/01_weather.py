# coding=utf-8
# 这是将单个城市历史一个月的天气信息爬取下来
import io
import sys
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import pymysql

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码, 防止控制台打印乱码

url = "http://www.tianqihoubao.com/weather/top/hefei.html"


# 获取网页内容
def get_soup(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 若请求不成功,抛出HTTPError 异常
        # r.encoding = 'gbk'
        soup = BeautifulSoup(r.text, 'lxml')
        return soup
    except requests.HTTPError:
        return "Request Error"


# 数据存储到csv文件
# def saveTocsv(data, fileName):
#     '''
#     将天气数据保存至csv文件
#     '''
#
#     # 城市  日期	天气状况	风力方向	最高温度	天气状况	风力方向	最低温度，用下面的数字分别代表
#     result_weather = pd.DataFrame(data, columns=['1', '2', '3', '4', '5', '6', '7', '8'])
#     result_weather.to_csv(fileName, index=False, encoding='gbk')
#     print('Save all weather success!')


# 数据存储到Mysql
def saveToMysql(data):
    '''
    将天气数据保存至MySQL数据库
    '''
    # 建立连接
    conn = pymysql.connect(host="localhost", port=3306, user='root', passwd='123456', database='weather1',
                           charset="utf8")
    # 获取游标
    cursor = conn.cursor()

    # 城市  日期	天气状况	风力方向	最高温度	天气状况	风力方向	最低温度
    sql = "INSERT INTO weather(city,date1 ,con,wind,maxtemp,con1,wind1,mintemp) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    data_list = np.ndarray.tolist(data)  # 将numpy数组转化为列表
    try:
        cursor.executemany(sql, data_list)
        print(cursor.rowcount)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()

    cursor.close()
    conn.close()


# 解析网页内容，得到数据
def get_data():
    soup = get_soup(url)
    all_weather = soup.find('div', class_="wdetail").find('table').find_all("tr")

    data = list()
    for tr in all_weather[2:]:
        td_li = tr.find_all("td")
        for td in td_li:
            s = td.get_text()
            data.append("".join(s.split()))

    res = np.array(data).reshape(-1, 8)
    return res


if __name__ == '__main__':
    data = get_data()
    # saveTocsv(data, "13.csv")
    saveToMysql(data)
