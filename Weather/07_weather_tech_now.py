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


def parse_page(html, city_name, city_kjy, city_zb):
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
    wea = soup.find_all(class_="wea")[0].text.strip()
    tem = soup.find_all(class_="tem")[0].text.strip()
    win = soup.find_all(class_="win")[0].span['title'].strip()
    leve1 = soup.find_all(class_="win")[0].i.text.strip()
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

    sql = "INSERT INTO tech_now(城市,科技园,科技园坐标,日期,时间实况, 当前温度,天气概况,风向,风力) VALUES ('%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
    city_name, city_kjy, city_zb, date, time1, tem, wea, win, leve1)

    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


def main():
    files = open('city_list_tech_now.txt', 'r', encoding='utf-8')
    city_all = files.readlines()

    try:
        for line in city_all:
            city_name_id = line.split('=')[0].replace("\n", "")
            city_jw = line.split('=')[1].replace("\n", "")
            city_name = city_name_id.split('-')[0].replace("\n", "")
            city_id = city_name_id.split('-')[1].replace("\n", "")
            city_kjy = city_jw.split('-')[0].replace("\n", "")
            city_zb = city_jw.split('-')[1].replace("\n", "")

            url = 'http://www.weather.com.cn/weather/' + city_id + '.shtml'

            html = get_page(url)

            # print(html)  # 输出用以检查全部内容

            parse_page(html, city_name, city_kjy, city_zb)
        files.close()
    except:
        print("error")


if __name__ == '__main__':
    main()
    print('success')

