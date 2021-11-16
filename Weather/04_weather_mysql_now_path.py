import requests
from bs4 import BeautifulSoup
import pymysql
from lxml import etree

conn = pymysql.connect(user='root', password='123456', host='localhost', database='new', port=3306, charset='utf8')
cursor = conn.cursor()


def get_page(url):
    try:
        headers = {
            # 'user-agent': 'Mozilla/5.0'
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'
        }
        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text  # 以字符串的形式来返回了网页的源码
    except:
        return 'error'


def parse_page(html, city_name):
    # soup = BeautifulSoup(html, 'lxml')
    """
    时间实况 -> time
    温度 -> tem
    相对湿度 -> zs h
    风向级数 -> zs w
    空气质量 -> zs pool
    """
    # time = soup.find('div', class_='sk mySkyNull').find('p', class_='time').find('span').get_text()
    #
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

    # 解析服务器响应的文件
    tree = etree.HTML(html)

    # 获取想要的数据  xpath的返回值是一个列表类型的数据
    time = tree.xpath("//div[@class='sk mySky']/p[@class='time']/span/text()")  # //*[@id="today"]/div[1]/div/p[1]/span
    tem = tree.xpath("//div[@class='sk mySky']/div[@class='tem']/text()")
    zs_h = tree.xpath("//div[@class='sk mySky']/div[@class='zs h']/text()")
    zs_w = tree.xpath("//div[@class='sk mySky']/div[@class='zs w']/text()")
    zs_pol = tree.xpath("//div[@class='sk mySky']/div[@class='zs pol']/span/a/text()")

    sql = "INSERT INTO test1(城市,时间实况, 温度,相对湿度,风向级数,空气质量) VALUES ('%s','%s', '%s', '%s', '%s', '%s')" % (
        city_name, time, tem, zs_h, zs_w, zs_pol)

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

            url = 'http://www.weather.com.cn/weather1d/' + city_id + '.shtml'

            html = get_page(url)
            # print(html)
            parse_page(html, city_name)  # ---> 出错
        files.close()
    except:
        print("error")


if __name__ == '__main__':
    main()
    print('success')
