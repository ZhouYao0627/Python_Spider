import time
import requests
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(user='root', password='123456', host='localhost', database='new', port=3306, charset='utf8')
cursor = conn.cursor()


def get_page(url):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0'
        }
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text  # 以字符串的形式来返回了网页的源码
    except:
        return 'error'


def parse_page(html, city_name):
    soup = BeautifulSoup(html, 'lxml')
    """
    时间实况 -> time
    温度 -> tem
    相对湿度 -> zs h
    风向级数 -> zs w
    空气质量 -> zs pool
    """

    data = soup.find(class_="t clearfix")
    date = data.li.h1.text
    # print("查询的日期：", date)
    wea = soup.find_all(class_="wea")[0].text.strip()
    # print("天气概况：", wea)
    tem = soup.find_all(class_="tem")[0].text.strip()
    # print("当前温度:", tem)
    win = soup.find_all(class_="win")[0].span['title'].strip()
    # print("风向:", win)
    leve1 = soup.find_all(class_="win")[0].i.text.strip()
    # print("风力:", leve1)
    # print("当前时间是：", time.asctime())
    time1 = time.asctime()

    # time = soup.find('div', class_='sk mySkyNull').find('p', class_='time').find('span').get_text()

    # tem1 = soup.find('div', 'sk mySkyNull').find('div', 'tem').find('span').get_text()
    # tem2 = soup.find('div', 'sk mySkyNull').find('div', 'tem').find('em').get_text()
    # tem = tem1 + tem2
    #
    # zs_h1 = soup.find('div', 'sk mySkyNull').find('div', 'zs h').find('span').get_text()
    # zs_h2 = soup.find('div', 'sk mySkyNull').find('div', 'zs h').find('em').get_text()
    # zs_h = zs_h1 + zs_h2
    #
    # zs_w1 = soup.find('div', 'sk mySkyNull').find('div', 'zs w').find('span').get_text()
    # zs_w2 = soup.find('div', 'sk mySkyNull').find('p', 'zs w').find('em').get_text()
    # zs_w = zs_w1 + zs_w2
    #
    # zs_pool = soup.find('div', 'sk mySkyNull').find('div', 'zs pool').find('span').find('a').get_text()

    # sql = "INSERT INTO test1(城市,时间实况, 温度,相对湿度,风向级数,空气质量) VALUES ('%s','%s', '%s', '%s', '%s', '%s')" % (
    #     city_name, time1, tem, zs_h, zs_w, zs_pool)

    sql = "INSERT INTO test2(城市,日期,时间实况, 当前温度,天气概况,风向,风力) VALUES ('%s','%s', '%s', '%s', '%s', '%s', '%s')" % (
        city_name, date, time1, tem, wea, win, leve1)

    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


def main():
    files = open('city_list_pre7.txt', 'r', encoding='utf-8')
    city_name_id = files.readlines()

    try:
        for line in city_name_id:
            city_name = line.split('-')[0].replace("\n", "")
            city_id = line.split('-')[1].replace("\n", "")

            url = 'http://www.weather.com.cn/weather/' + city_id + '.shtml'

            html = get_page(url)

            # print(html)  # 输出用以检查全部内容

            parse_page(html, city_name)
        files.close()
    except:
        print("error")


if __name__ == '__main__':
    main()
    print('success')

"""
# import re
# from bs4 import BeautifulSoup
# import requests
# import pymysql
# import time
# 
# # 1 链接本地的数据库
# conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='new', charset='utf8')
# 
# # 创建表city_weather_code ，id是自增的并且唯一，同时设为主键；city_name，city_code分别对应城市名字和编码
# create_table_sql = "CREATE TABLE IF NOT EXISTS city_weather_code (" \
#                    "id INT PRIMARY KEY AUTO_INCREMENT," \
#                    "city_name VARCHAR(30) NOT NULL ," \
#                    "city_code INT NOT NULL)  "
# cursor = conn.cursor()  # 获取游标
# cursor.execute(create_table_sql)  # 执行创建语句
# conn.commit()  # 使执行创建语句生效
# # 打开文件按行读取数据
# with open("city_list_now.txt", 'r', encoding='utf-8') as f:  # 读的模式打开
#     res = f.readlines()  # 一行行读取文件，
#     for i in res:  # 遍历文件每一行，先去空格然后以‘’=‘’号分割。每行得到一个列表
#         if i != "\n":
#             data = i.split("-")
#             citycode = data[1]  # 把编码赋值给citycode
#             cityname = data[0]  # 把城市名赋值给cityname
# 
#             insert_sql = "INSERT INTO city_weather_code(city_name,city_code) VALUE ('%s','%s')" % (
#                 cityname.strip(), citycode.strip())  # 把数据插入数据库
#             cursor.execute(insert_sql)
#             conn.commit()
# conn.close()
# 
# 
# # 查询代码封装成函数
# def check_code(check_name):
#     conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='new', charset='utf8')
#     cursor = conn.cursor()
#     select_mysql = "SELECT city_code FROM city_weather_code WHERE city_name ='%s'" % check_name
#     cursor.execute(select_mysql)
#     res = cursor.fetchone()  # 返回值是一个元组
#     # print(res)
#     conn.commit()
#     cursor.close()
#     conn.close()
#     return res[0]
# 
# 
# # 拼接url封装成函数
# def url(code):
#     # 中国天气网址天气页面url:http://www.weather.com.cn/weather/101180101.shtml,
#     # 其中101180101，即是各城市的代码。代码对应城市，拼接出地址即可
#     raw_url = "http://www.weather.com.cn/weather/"
#     url = raw_url + str(code) + ".shtml"
#     return url
# 
# 
# # 获取天气
# def get_weather(url):
#     Header = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"}
#     res = requests.get(url, headers=Header)
#     soup = BeautifulSoup(res.content, 'html.parser')
#     # 下面代码解释出当前的日期、温度、天气、风向、风力
#     # 关键是，代码写死了，爬取网站代码一改，又要跟着调整。
#     data = soup.find(class_="t clearfix")
#     date = data.li.h1.text
#     print("查询的日期：", date)
#     wea = soup.find_all(class_="wea")[0].text.strip()
#     print("天气概况：", wea)
#     tem = soup.find_all(class_="tem")[0].text.strip()
#     print("当前温度:", tem)
#     win = soup.find_all(class_="win")[0].span['title'].strip()
#     print("风向:", win)
#     leve1 = soup.find_all(class_="win")[0].i.text.strip()
#     print("风力:", leve1)
#     print("当前时间是：", time.asctime())
# 
# 
# 
# if __name__ == "__main__":
#     while True:
#         print("--------欢迎使用py自己动手查天气--------")
#         check_name = input("请输入要查询的城市[按q]退出>>>").strip()
#         if check_name == "q":
#             break
#         else:
#             try:
#                 code = check_code(check_name)  # 根据输入的内容数据库取对应的城市代码
#                 print("查询城市代码成功！")
#                 url = url(code)  # 拼接url
#                 print("正在获取天气，请稍后。。。")
#                 get_weather(url)  # 查询天气并输出
#             except:
#                 print("查询失败，请输入正确的城市名称，例如[北京]、[天河]，市或区县名称。")
"""

"""
# import requests
# from bs4 import BeautifulSoup
# import pymysql
# 
# conn = pymysql.connect(user='root', password='123456', host='localhost', database='new', port=3306, charset='utf8')
# cursor = conn.cursor()
# 
# 
# def get_page(url):
#     try:
#         headers = {
#             'user-agent': 'Mozilla/5.0'
#         }
#         response = requests.get(url=url, headers=headers)
#         response.raise_for_status()
#         response.encoding = response.apparent_encoding
#         return response.text  # 以字符串的形式来返回了网页的源码
#     except:
#         return 'error'
# 
# 
# def parse_page(html, city_name):
#     soup = BeautifulSoup(html, 'lxml')
#     
#     时间实况 -> time
#     温度 -> tem
#     相对湿度 -> zs h
#     风向级数 -> zs w
#     空气质量 -> zs pool
#     
#     time = soup.find('div', class_='sk mySkyNull').find('p', class_='time').find('span').get_text()
# 
#     tem1 = soup.find('div', 'sk mySkyNull').find('div', 'tem').find('span').get_text()
#     tem2 = soup.find('div', 'sk mySkyNull').find('div', 'tem').find('em').get_text()
#     tem = tem1 + tem2
# 
#     zs_h1 = soup.find('div', 'sk mySkyNull').find('div', 'zs h').find('span').get_text()
#     zs_h2 = soup.find('div', 'sk mySkyNull').find('div', 'zs h').find('em').get_text()
#     zs_h = zs_h1 + zs_h2
# 
#     zs_w1 = soup.find('div', 'sk mySkyNull').find('div', 'zs w').find('span').get_text()
#     zs_w2 = soup.find('div', 'sk mySkyNull').find('p', 'zs w').find('em').get_text()
#     zs_w = zs_w1 + zs_w2
# 
#     zs_pool = soup.find('div', 'sk mySkyNull').find('div', 'zs pool').find('span').find('a').get_text()
# 
#     sql = "INSERT INTO test1(城市,时间实况, 温度,相对湿度,风向级数,空气质量) VALUES ('%s','%s', '%s', '%s', '%s', '%s')" % (
#         city_name, time, tem, zs_h, zs_w, zs_pool)
# 
#     try:
#         cursor.execute(sql)
#         conn.commit()
#     except Exception as e:
#         print(e)
#         conn.rollback()
# 
# 
# def main():
#     files = open('city_list_pre7.txt', 'r', encoding='utf-8')
#     city_name_id = files.readlines()
# 
#     try:
#         for line in city_name_id:
#             city_name = line.split('-')[0].replace("\n", "")
#             city_id = line.split('-')[1].replace("\n", "")
# 
#             url = 'http://www.weather.com.cn/weather1d/' + city_id + '.shtml'
# 
#             html = get_page(url)
# 
#             # print(html)  # 输出用以检查全部内容
# 
#             parse_page(html, city_name)  # ---> 出错
#         files.close()
#     except:
#         print("error")
# 
# 
# if __name__ == '__main__':
#     main()
#     print('success')

"""
