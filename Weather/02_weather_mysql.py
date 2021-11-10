# 失败
# 这是将未来七天的天气信息给爬取下来
import requests
from bs4 import BeautifulSoup
import re  # re --- 正则表达式操作
import pymysql
import numpy as np

result_list_wt = []


# 获取网页内容
def get_page(url):
    try:
        kv = {
            'user-agent': 'Mozilla/5.0'
        }
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'


# 解析网页内容，得到数据
def parse_page(html, return_list):
    soup = BeautifulSoup(html, 'html.parser')
    day_list = soup.find('ul', 't clearfix').find_all('li')
    for day in day_list:
        date = day.find('h1').get_text()
        wea = day.find('p', 'wea').get_text()
        if day.find('p', 'tem').find('span'):
            hightem = day.find('p', 'tem').find('span').get_text()
        else:
            hightem = ''
        lowtem = day.find('p', 'tem').find('i').get_text()
        win = re.findall('(?<= title=").*?(?=")', str(day.find('p', 'win').find('em')))
        wind = '-'.join(win)
        level = day.find('p', 'win').find('i').get_text()
        return_list.append([date, wea, lowtem, hightem, wind, level])

    # 建立连接
    conn = pymysql.connect(host="localhost", port=3306, user='root', passwd='123456', database='weather2',
                           charset="utf8")
    # 获取游标
    cursor = conn.cursor()

    # 日期 天气 最低温 高温　风向　风力
    sql = "INSERT INTO weather(date1,temp ,mintemp,maxtemp,wind1,wind2) VALUES(%s,%s,%s,%s,%s,%s)"
    data_list = np.ndarray.tolist(return_list)  # 将numpy数组转化为列表
    try:
        cursor.executemany(sql, data_list)
        print(cursor.rowcount)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()

    cursor.close()
    conn.close()


def print_res(return_list):
    tplt = '{0:<10}\t{1:^10}\t{2:^10}\t{3:{6}^10}\t{4:{6}^10}\t{5:{6}^5}'
    result_list_wt.append(tplt.format('日期', '天气', '最低温', '最高温', '风向', '风力', chr(12288)) + "\n")
    for i in return_list:
        result_list_wt.append(tplt.format(i[0], i[1], i[2], i[3], i[4], i[5], chr(12288)) + "\n")


def main():
    # 城市-城市码txt
    files = open('city_list.txt', "r", encoding='utf-8')
    city_name_id = files.readlines()
    try:
        # 获取txt-list
        for line in city_name_id:
            name_id = line.split('-')[1].replace("['", "").replace("\n", "")
            url = 'http://www.weather.com.cn/weather/' + name_id + '.shtml'
            city_name = line.split('-')[0].replace("['", "").replace("\n", "")
            city_china = "\n" + "城市名 : " + city_name + "\n"
            result_list_wt.append(city_china)
            html = get_page(url)
            wea_list = []
            parse_page(html, wea_list)
            print_res(wea_list)
        files.close()
    except:
        print("error")

    # 将获取结果写入到文件内
    msgs = ''.join(result_list_wt)
    # print(msgs)
    with open('weather.China.txt', "w+") as file:
        file.write(msgs)


if __name__ == '__main__':
    main()
