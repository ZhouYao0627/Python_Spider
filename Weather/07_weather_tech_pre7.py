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


def parse_page(html, city_name, city_kjy, city_zb):
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

        sql = "INSERT INTO tech_pre7(城市,科技园,科技园坐标,日期,天气,最高温度,最低温度,风向,风速等级) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            city_name, city_kjy, city_zb, date, wea, hightem, lowtem, wind, level)

        try:
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()


def main():
    files = open('city_list_tech_pre7.txt', 'r', encoding='utf-8')
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

            html = get_page(url)  # 获取网页数据

            # print(html)  # 输出用以检查全部内容

            parse_page(html, city_name, city_kjy, city_zb)  # 解析

        files.close()
    except:
        print("error")


if __name__ == '__main__':
    main()
    print('success')
