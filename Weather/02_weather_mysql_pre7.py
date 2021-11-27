# third test
# 这是将未来七天的天气信息给爬取下来并保存到数据库
import requests
from bs4 import BeautifulSoup
import pymysql

# 打开数据库连接，并使用cursor()建立一个游标对象
conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='zgtq', port=3306, charset='utf8')
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
    day_list = soup.find('ul', 't clearfix').find_all('li')
    for day in day_list:
        date = day.find('h1').get_text()
        wea = day.find('p', 'wea').get_text()

        if day.find('p', 'tem').find('span'):
            hightem = day.find('p', 'tem').find('span').get_text()
        else:
            hightem = ''
        lowtem = day.find('p', 'tem').find('i').get_text()
        wind = day.find('p', 'win').find('em').find('span').attrs['title']
        level = day.find('p', 'win').find('i').get_text()

        sql = "INSERT INTO future7(城市,城市坐标,日期,天气,最高温度,最低温度,风向,风速等级) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            city_name, city_jw, date, wea, hightem, lowtem, wind, level)

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

            # sql = "INSERT INTO test1(城市,日期,天气,最高温度,最低温度,风向,风速等级) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            #     city_name, ' ', ' ', ' ', ' ', ' ', ' ')
            #
            # try:
            #     cursor.execute(sql)
            #     conn.commit()
            # except Exception as e:
            #     print(e)
            #     conn.rollback()

            html = get_page(url)  # 获取网页数据

            # print(html)  # 输出用以检查全部内容

            parse_page(html, city_name, city_jw)  # 解析
            print(city_name)
        files.close()
    except:
        print("error")


if __name__ == '__main__':
    main()
    print('success')

"""
# second test
import requests
from bs4 import BeautifulSoup
import pymysql

# 打开数据库连接，并使用cursor()建立一个游标对象
conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='weather1', port=3306, charset='utf8')
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


def parse_page(html):
    soup = BeautifulSoup(html, 'lxml')
    day_list = soup.find('ul', 't clearfix').find_all('li')
    for day in day_list:
        date = day.find('h1').get_text()
        wea = day.find('p', 'wea').get_text()

        if day.find('p', 'tem').find('span'):
            hightem = day.find('p', 'tem').find('span').get_text()
        else:
            hightem = ''
        lowtem = day.find('p', 'tem').find('i').get_text()
        wind = day.find('p', 'win').find('em').find('span').attrs['title']
        level = day.find('p', 'win').find('i').get_text()


        sql = "INSERT INTO testweather3(日期,天气,最高温度,最低温度,风向,风速等级) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (
            date, wea, hightem, lowtem, wind, level)

        try:
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()


def main():
    files = open('city_list.txt', 'r', encoding='utf-8')
    city_name_id = files.readlines()

    try:
        for line in city_name_id:
            city_name = line.split('-')[0].replace("\n", "")
            city_id = line.split('-')[1].replace("\n", "")
            url = 'http://www.weather.com.cn/weather/' + city_id + '.shtml'

            sql = "INSERT INTO testweather3(日期,天气,最高温度,最低温度,风向,风速等级) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (
                city_name, ' ', ' ', ' ', ' ', ' ')

            try:
                cursor.execute(sql)
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()

            html = get_page(url)  # 获取网页数据
            parse_page(html)  # 解析

        files.close()
    except:
        print("error2")


if __name__ == '__main__':
    main()
    print('success')
"""

"""
# first test
import requests
from bs4 import BeautifulSoup
import pymysql

result_list_wt = []


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


def parse_page(html):
    soup = BeautifulSoup(html, 'lxml')
    day_list = soup.find('ul', 't clearfix').find_all('li')
    for day in day_list:
        date = day.find('h1').get_text()
        wea = day.find('p', 'wea').get_text()

        if day.find('p', 'tem').find('span'):
            hightem = day.find('p', 'tem').find('span').get_text()
        else:
            hightem = 'wu'
        lowtem = day.find('p', 'tem').find('i').get_text()
        wind = day.find('p', 'win').find('em').find('span').attrs['title']
        level = day.find('p', 'win').find('i').get_text()

        # return_list.append([date, wea, lowtem, hightem, wind, level])

        # 打开数据库连接，并使用cursor()建立一个游标对象
        conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='weather1', port=3306, charset='utf8')
        cursor = conn.cursor()

        sql = "INSERT INTO testweather1(日期,天气,最高温度,最低温度,风向,风速等级) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (
            date, wea, hightem, lowtem, wind, level)

        try:
            cursor.execute(sql)  #
            conn.commit()  # 提交
        except Exception as e:
            print(e)
            conn.rollback()


# def print_res(return_list):
#     tplt = '{0:<10}\t{1:{6}^10}\t{2:{6}^10}\t{3:{6}^10}\t{4:{6}^10}\t{5:{6}^10}'
#     result_list_wt.append(tplt.format('日期', '天气', '最高温度', '最低温度', '风向', '风力等级', chr(12288)) + "\n")
#     for i in return_list:
#         result_list_wt.append(
#             tplt.format(i[0], i[1], i[2], i[3], i[4], i[5], chr(12288)) + "\n")  # 宽度不够时采用中文空格填充，中文空格的编码为chr(12288)


def main():
    files = open('city_list.txt', 'r', encoding='utf-8')
    city_name_id = files.readlines()

    try:
        for line in city_name_id:
            # city_name = line.split('-')[0].replace("\n", "")
            city_id = line.split('-')[1].replace("\n", "")
            # http://www.weather.com.cn/weather1d/101030100.shtml#input
            url = 'http://www.weather.com.cn/weather/' + city_id + '.shtml'
            # url = 'http://www.weather.com.cn/weather/101020100.shtml'

            # city_china = "\n" + "城市名：" + city_name + "\n"
            # result_list_wt.append(city_china)

            html = get_page(url)  # 获取网页数据

            wea_list = []
            # parse_page(html, wea_list)  # 解析   ---> 出错
            parse_page(html)  # 解析   ---> 出错

            # print_res(wea_list)
        files.close()
    except:
        print("error2")

    # 将获取结果写入到文件内
    # msgs = ''.join(result_list_wt)
    # with open('weather.China_mysql', 'w', encoding='utf-8') as fp:
    #     fp.write(msgs)


if __name__ == '__main__':
    main()

"""
