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

# http://www.weather.com.cn/weather1d/101221107.shtml   天长
# http://www.weather.com.cn/weather1d/101190105.shtml  六合
# http://forecast.weather.com.cn/town/weather1dn/101190101064.shtml  板桥新城
# http://forecast.weather.com.cn/town/weather1dn/101190107005.shtml  盘城

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

def parse_page1(html, city_name):
    tree = etree.HTML(html)

    time = tree.xpath("//*[@id='today']/div[1]/div/p[1]/span/text()")[0]
    tem = tree.xpath("//*[@id='today']/div[1]/div/div[3]/span/text()")[0] + '℃'
    zs_h1 = tree.xpath("//*[@id='today']/div[1]/div/div[1]/span/text()")[0]
    zs_h2 = tree.xpath("//*[@id='today']/div[1]/div/div[1]/em/text()")[0]
    zs_h = zs_h1 + zs_h2

    zs_w1 = tree.xpath("//*[@id='today']/div[1]/div/div[2]/span/text()")[0]
    zs_w2 = tree.xpath("//*[@id='today']/div[1]/div/div[2]/em/text()")[0]
    zs_w = zs_w1 + zs_w2

    zs_pol = tree.xpath("//*[@id='today']/div[1]/div/div[5]/span/a/text()")[0]

    sql = "INSERT INTO test1(城市,时间实况, 温度,相对湿度,风向级数,空气质量) VALUES ('%s','%s', '%s', '%s', '%s', '%s')" % (
        city_name, time, tem, zs_h, zs_w, zs_pol)

    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


def main():
    files = open('city_list_four.txt', 'r', encoding='utf-8')
    city_name_id = files.readlines()

    try:
        for line in city_name_id:
            city_name = line.split('-')[0].replace("\n", "")
            city_id = line.split('-')[1].replace("\n", "")

            if (city_id == '101221107' or city_id == '101190105'):
                url = 'http://www.weather.com.cn/weather1d/' + city_id + '.shtml'
                web.get(url)
                html = web.page_source  # 得到页面element的html代码
                parse_page1(html, city_name)
            else:
                url = 'http://forecast.weather.com.cn/town/weather1dn/' + city_id + '.shtml'
                html = get_page(url)
                parse_page2(html, city_name)

        files.close()
    except:
        print("error")


if __name__ == '__main__':
    main()
    print('success')
