import requests
from lxml import etree
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options  # 不显示页面
import pymysql

# 不显示浏览器使用的过程
opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
# -------------------------------------
web = Chrome(options=opt)  # 把参数设置到浏览器

conn = pymysql.connect(user='root', password='123456', host='localhost', database='zgtq', port=3306, charset='utf8')
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


def time_all(tree):
    # 08-13时
    #                  /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/ul[5]/li[1]/text() # 08  --->
    #                  /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/ul[5]/li[2]/text() # 09
    #                  ......
    #                  /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/ul[5]/li[4]/text() # 11  --->
    #                  /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/ul[5]/li[6]/text() # 13

    # 02时-07时
    #                  /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/ul[5]/li[1]/text() # 02  --->
    #                  /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/ul[5]/li[2]/text() # 03
    #                  ......
    #                  /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/ul[5]/li[4]/text() # 05  --->
    #                  /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/ul[5]/li[6]/text() # 07

    # 20时-01时
    #                  /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/ul[5]/li[1]/text() # 20  --->
    #                  /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/ul[5]/li[2]/text() # 21
    #                  ......
    #                  /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/ul[5]/li[4]/text() # 23  --->
    #                  /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/ul[5]/li[6]/text() # 01

    # 14时-19时
    #                  /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/ul[5]/li[1]/text() # 14  --->
    #                  /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/ul[5]/li[2]/text() # 15
    #                  ......
    #                  /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/ul[5]/li[4]/text() # 17  --->
    #                  /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/ul[5]/li[6]/text() # 19

    dir = []

    # 14时-19时
    # time = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/ul[5]/li[1]/text()")
    # time = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/ul[5]/li[" + (i + 1) + "]/text()")
    # dir.append(time)
    time_14 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/ul[5]/li[1]/text()")
    time_17 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/ul[5]/li[4]/text()")
    time_20 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/ul[5]/li[1]/text()")
    time_23 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/ul[5]/li[4]/text()")
    time_02 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/ul[5]/li[1]/text()")
    time_05 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/ul[5]/li[4]/text()")
    time_08 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/ul[5]/li[1]/text()")
    time_11 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/ul[5]/li[4]/text()")
    dir.append(time_14)
    dir.append(time_17)
    dir.append(time_20)
    dir.append(time_23)
    dir.append(time_02)
    dir.append(time_05)
    dir.append(time_08)
    dir.append(time_11)

    return dir


def wea_all(tree):
    dir = []
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/ul[2]/li[1]
    wea_14 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/ul[2]/li[1]/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/ul[2]/li[4]
    wea_17 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/ul[2]/li[4]/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/ul[2]/li[1]
    wea_20 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/ul[2]/li[1]/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/ul[2]/li[4]
    wea_23 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/ul[2]/li[4]/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/ul[2]/li[1]
    wea_02 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/ul[2]/li[1]/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/ul[2]/li[4]
    wea_05 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/ul[2]/li[4]/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/ul[2]/li[1]
    wea_08 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/ul[2]/li[1]/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/ul[2]/li[4]
    wea_11 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/ul[2]/li[4]/text()")
    dir.append(wea_14)
    dir.append(wea_17)
    dir.append(wea_20)
    dir.append(wea_23)
    dir.append(wea_02)
    dir.append(wea_05)
    dir.append(wea_08)
    dir.append(wea_11)

    return dir


def tem_all(tree):
    dir = []
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/div/ul/li[1]/span
    tem_14 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/div/ul/li[1]/span/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/div/ul/li[4]/span
    tem_17 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/div/ul/li[4]/span/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/div/ul/li[1]/span
    tem_20 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/div/ul/li[1]/span/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/div/ul/li[4]/span
    tem_23 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/div/ul/li[4]/span/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/div/ul/li[1]/span
    tem_02 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/div/ul/li[1]/span/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/div/ul/li[4]/span
    tem_05 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/div/ul/li[4]/span/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/div/ul/li[1]/span
    tem_08 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/div/ul/li[1]/span/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/div/ul/li[4]/span
    tem_11 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/div/ul/li[4]/span/text()")

    dir.append(tem_14)
    dir.append(tem_17)
    dir.append(tem_20)
    dir.append(tem_23)
    dir.append(tem_02)
    dir.append(tem_05)
    dir.append(tem_08)
    dir.append(tem_11)

    return dir


def winf_all(tree):
    dir = []
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/ul[3]/li[1]
    winf_14 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/ul[3]/li[1]/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/ul[3]/li[4]
    winf_17 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/ul[3]/li[4]/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/ul[3]/li[1]
    winf_20 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/ul[3]/li[1]/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/ul[3]/li[4]
    winf_23 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/ul[3]/li[4]/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/ul[3]/li[1]
    winf_02 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/ul[3]/li[1]/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/ul[3]/li[4]
    winf_05 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/ul[3]/li[4]/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/ul[3]/li[1]
    winf_08 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/ul[3]/li[1]/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/ul[3]/li[4]
    winf_11 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/ul[3]/li[4]/text()")

    dir.append(winf_14)
    dir.append(winf_17)
    dir.append(winf_20)
    dir.append(winf_23)
    dir.append(winf_02)
    dir.append(winf_05)
    dir.append(winf_08)
    dir.append(winf_11)

    return dir


def winl_all(tree):
    dir = []
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/ul[4]/li[1]
    winl_14 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/ul[4]/li[1]/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/ul[4]/li[4]
    winl_17 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[1]/ul[4]/li[4]/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/ul[4]/li[1]
    winl_20 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/ul[4]/li[1]/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/ul[4]/li[4]
    winl_23 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[2]/ul[4]/li[4]/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/ul[4]/li[1]
    winl_02 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/ul[4]/li[1]/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/ul[4]/li[4]
    winl_05 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/ul[4]/li[4]/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/ul[4]/li[1]
    winl_08 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/ul[4]/li[1]/text()")
    # /html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/ul[4]/li[4]
    winl_11 = tree.xpath("/html/body/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/ul[4]/li[4]/text()")

    dir.append(winl_14)
    dir.append(winl_17)
    dir.append(winl_20)
    dir.append(winl_23)
    dir.append(winl_02)
    dir.append(winl_05)
    dir.append(winl_08)
    dir.append(winl_11)

    return dir


def parse_page(html, city_name):
    tree = etree.HTML(html)

    time_list = time_all(tree)
    wea_list = wea_all(tree)
    tem_list = tem_all(tree)
    winf_list = winf_all(tree)
    winl_list = winl_all(tree)

    print(city_name)

    for i in range(8):
        time = time_list[i][0]
        wea = wea_list[i][0]
        tem = tem_list[i][0]
        winf = winf_list[i][0]
        winl = winl_list[i][0]

        sql = "INSERT INTO period(城市,时间, 天气,温度,风向,风向级数) VALUES ('%s','%s', '%s', '%s', '%s', '%s')" % (
            city_name, time, wea, tem, winf, winl)

        try:
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()


def main():
    files = open('city_list_new_url.txt', 'r', encoding='utf-8')
    city_name_id = files.readlines()

    try:
        for line in city_name_id:
            city_name = line.split('-')[0].replace("\n", "")
            city_id = line.split('-')[1].replace("\n", "")

            url = 'https://www.tianqi.com/beijing/'
            # url = 'https://www.tianqi.com/' + city_id + '/'
            web.get(url)
            html = web.page_source  # 得到页面element的html代码
            parse_page(html, city_name)

        files.close()
    except:
        print("error")


if __name__ == '__main__':
    main()
    print('success')

# import time
# import requests
# from bs4 import BeautifulSoup
# import pymysql
#
# conn = pymysql.connect(user='root', password='123456', host='localhost', database='zgtq', port=3306, charset='utf8')
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
#     data = soup.find(class_="day7")
#     wea = data.find(class_="txt txt2").find_all("li")
#     time1 = data.find(class_="txt canvas_hour").find(class_="w95")
#     tem = data.find(class_="zxt_shuju1").find_all("ul")
#     winf = data.find(class_="txt").find_all(class_="w95")
#     winl = data.find(class_="txt").find_all(class_="w95 mgtop5")
#
#     sql = "INSERT INTO period(城市,时间, 天气,温度,风向,风向级数) VALUES ('%s','%s', '%s', '%s', '%s', '%s')" % (
#         city_name, time1, wea,tem, winf, winl)
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
#     files = open('city_list_new_url.txt', 'r', encoding='utf-8')
#     city_name_id = files.readlines()
#
#     try:
#         for line in city_name_id:
#             city_name = line.split('-')[0].replace("\n", "")
#             city_id = line.split('-')[1].replace("\n", "")
#
#             # https://www.tianqi.com/beijing/
#             url = 'https://www.tianqi.com/' + city_id + '/'
#
#             html = get_page(url)
#
#             # print(html)  # 输出用以检查全部内容
#
#             parse_page(html, city_name)
#         files.close()
#     except:
#         print("error")
#
#
# if __name__ == '__main__':
#     main()
#     print('success')
#
