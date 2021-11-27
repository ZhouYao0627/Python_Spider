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


def parse_page1(html, city_name, city_jw):
    tree = etree.HTML(html)

    time = tree.xpath("//*[@id='today']/div[1]/div/p[1]/span/text()")[0]
    tem = tree.xpath("//*[@id='today']/div[1]/div/div[3]/span/text()")[0] + '℃'  # 当前温度
    zs_h1 = tree.xpath("//*[@id='today']/div[1]/div/div[1]/span/text()")[0]
    zs_h2 = tree.xpath("//*[@id='today']/div[1]/div/div[1]/em/text()")[0]
    zs_h = zs_h1 + zs_h2

    zs_w1 = tree.xpath("//*[@id='today']/div[1]/div/div[2]/span/text()")[0]
    zs_w2 = tree.xpath("//*[@id='today']/div[1]/div/div[2]/em/text()")[0]
    zs_w = zs_w1 + zs_w2

    zs_pol = tree.xpath("//*[@id='today']/div[1]/div/div[5]/span/a/text()")[0]

    sql = "INSERT INTO tech_four_place(城市,城市坐标,时间实况, 温度,相对湿度,风向级数,空气质量) VALUES ('%s','%s', '%s', '%s', '%s', '%s', '%s')" % (
        city_name, city_jw, time, tem, zs_h, zs_w, zs_pol)

    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


def parse_page2(html, city_name, city_jw):
    tree = etree.HTML(html)

    time = tree.xpath("/html/body/div[4]/div[3]/div[2]/div[1]/div/span/text()")[0]
    tem = tree.xpath("/html/body/div[4]/div[3]/div[2]/div[3]/span[1]/text()")[0] + '℃'
    zs_h = tree.xpath("/html/body/div[4]/div[3]/div[2]/p[2]/span/text()")[0]

    zs_w = tree.xpath("/html/body/div[4]/div[3]/div[2]/p[1]/span/text()")[0]

    zs_pol = ''

    sql = "INSERT INTO tech_four_place(城市,城市坐标,时间实况, 温度,相对湿度,风向级数,空气质量) VALUES ('%s','%s', '%s', '%s', '%s', '%s', '%s')" % (
        city_name, city_jw, time, tem, zs_h, zs_w, zs_pol)

    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


def main():
    files = open('city_list_tech_four_place.txt', 'r', encoding='utf-8')
    city_all = files.readlines()

    try:
        for line in city_all:
            city_name_id = line.split('=')[0].replace("\n", "")
            city_jw = line.split('=')[1].replace("\n", "")
            city_name = city_name_id.split('-')[0].replace("\n", "")
            city_id = city_name_id.split('-')[1].replace("\n", "")

            if (city_id == '101221107' or city_id == '101190105'):
                url = 'http://www.weather.com.cn/weather1d/' + city_id + '.shtml'
                web.get(url)
                html = web.page_source  # 得到页面element的html代码
                parse_page1(html, city_name, city_jw)
            else:
                url = 'http://forecast.weather.com.cn/town/weather1dn/' + city_id + '.shtml'
                web.get(url)
                html = get_page(url)
                parse_page2(html, city_name, city_jw)

        files.close()
    except:
        print("error")


if __name__ == '__main__':
    main()
    print('success')
