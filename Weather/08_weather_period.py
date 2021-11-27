import time
import requests
from bs4 import BeautifulSoup
import pymysql

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


def parse_page(html, city_name, city_jw):
    soup = BeautifulSoup(html, 'lxml')

    data = soup.find(class_="curve_livezs")
    time1 = data.find(class_="time")
    tem = data.find(class_="tem").find_all("em")
    winf = data.find(class_="winf").find_all("em")
    winl = data.find(class_="winl").find_all("em")

    sql = "INSERT INTO period(城市,坐标, 段时间,段温度,段风向,段风向级数) VALUES ('%s','%s', '%s', '%s', '%s', '%s')" % (
        city_name, city_jw, time1, tem, winf, winl)

    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


def main():
    files = open('city_list_dijishi.txt', 'r', encoding='utf-8')
    city_all = files.readlines()

    try:
        for line in city_all:
            city_name_id = line.split('=')[0].replace("\n", "")
            city_jw = line.split('=')[1].replace("\n", "")
            city_name = city_name_id.split('-')[0].replace("\n", "")
            city_id = city_name_id.split('-')[1].replace("\n", "")

            url = 'http://www.weather.com.cn/weather/' + city_id + '.shtml'

            html = get_page(url)

            # print(html)  # 输出用以检查全部内容

            parse_page(html, city_name, city_jw)
            print(city_name)
        files.close()
    except:
        print("error")


if __name__ == '__main__':
    main()
    print('success')

# import requests
# from bs4 import BeautifulSoup
# import pymysql
# from lxml import etree
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
# def parse_page(html, city_name, city_jw):
#     # soup = BeautifulSoup(html, 'lxml')
#     """
#     时间实况 -> time
#     温度 -> tem
#     相对湿度 -> zs h
#     风向级数 -> zs w
#     空气质量 -> zs pool
#     """
#     # time = soup.find('div', class_='sk mySkyNull').find('p', class_='time').find('span').get_text()
#     #
#     # tem1 = soup.find('div', 'sk mySkyNull').find('div', 'tem').find('span').get_text()
#     # tem2 = soup.find('div', 'sk mySkyNull').find('div', 'tem').find('em').get_text()
#     # tem = tem1 + tem2
#     #
#     # zs_h1 = soup.find('div', 'sk mySkyNull').find('div', 'zs h').find('span').get_text()
#     # zs_h2 = soup.find('div', 'sk mySkyNull').find('div', 'zs h').find('em').get_text()
#     # zs_h = zs_h1 + zs_h2
#     #
#     # zs_w1 = soup.find('div', 'sk mySkyNull').find('div', 'zs w').find('span').get_text()
#     # zs_w2 = soup.find('div', 'sk mySkyNull').find('p', 'zs w').find('em').get_text()
#     # zs_w = zs_w1 + zs_w2
#     #
#     # zs_pool = soup.find('div', 'sk mySkyNull').find('div', 'zs pool').find('span').find('a').get_text()
#
#     # 解析服务器响应的文件
#
#     # //*[@id='curve']/div[1]/em  ---> class="time"
#     # //*[@id='curve']/div[4]/em  ---> class="tem"
#     # //*[@id='curve']/div[5]/em  ---> class="winf"
#     # //*[@id='curve']/div[6]/em  ---> class="winl"
#
#     tree = etree.HTML(html)
#
#     # 获取想要的数据  xpath的返回值是一个列表类型的数据
#     time = tree.xpath("//*[@id='curve']/div[1]/em/text()")
#     tem = tree.xpath("//*[@id='curve']/div[4]/em/text()")
#     winf = tree.xpath("//*[@id='curve']/div[5]/em/text()")
#     winl = tree.xpath("//*[@id='curve']/div[6]/em/text()")
#
#     sql = "INSERT INTO period(城市,坐标, 段时间,段温度,段风向,段风向级数) VALUES ('%s','%s', '%s', '%s', '%s', '%s')" % (
#         city_name, city_jw, time, tem, winf, winl)
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
#     files = open('city_list_dijishi.txt', 'r', encoding='utf-8')
#     city_all = files.readlines()
#
#     try:
#         for line in city_all:
#             city_name_id = line.split('=')[0].replace("\n", "")
#             city_jw = line.split('=')[1].replace("\n", "")
#             city_name = city_name_id.split('-')[0].replace("\n", "")
#             city_id = city_name_id.split('-')[1].replace("\n", "")
#
#             url = 'http://www.weather.com.cn/weather1d/' + city_id + '.shtml'
#
#             html = get_page(url)
#             # print(html)
#             parse_page(html, city_name, city_jw)
#         files.close()
#     except:
#         print("error")
#
#
# if __name__ == '__main__':
#     main()
#     print('success')
