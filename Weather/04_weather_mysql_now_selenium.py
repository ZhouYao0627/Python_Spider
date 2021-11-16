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
# url = "http://www.weather.com.cn/weather1d/101010100.shtml"

# web.get(url)
# text = web.page_source  # 得到页面element的html代码
# tree = etree.HTML(text)

# time = tree.xpath("//*[@id='today']/div[1]/div/p[1]/span/text()")[0]  # 19:35 实况
# tem = tree.xpath("//*[@id='today']/div[1]/div/div[4]/span/text()")[0] + '℃'  # 6℃
# zs_h1 = tree.xpath("//*[@id='today']/div[1]/div/div[2]/span/text()")[0]
# zs_h2 = tree.xpath("//*[@id='today']/div[1]/div/div[2]/em/text()")[0]
# zs_h = zs_h1 + zs_h2  # # 相对湿度67%
#
# zs_w1 = tree.xpath("//*[@id='today']/div[1]/div/div[3]/span/text()")[0]
# zs_w2 = tree.xpath("//*[@id='today']/div[1]/div/div[3]/em/text()")[0]
# zs_w = zs_w1 + zs_w2  # 东北风1级
#
# zs_pol = tree.xpath("//*[@id='today']/div[1]/div/div[6]/span/a/text()")[0]  # 67良

conn = pymysql.connect(user='root', password='123456', host='localhost', database='new', port=3306, charset='utf8')
cursor = conn.cursor()

files = open('city_list_now.txt', 'r', encoding='utf-8')
city_name_id = files.readlines()

try:
    for line in city_name_id:
        city_name = line.split('-')[0].replace("\n", "")
        city_id = line.split('-')[1].replace("\n", "")

        url = 'http://www.weather.com.cn/weather1d/' + city_id + '.shtml'
        # url = 'http://www.weather.com.cn/weather1d/101160101.shtml'

        web.get(url)
        text = web.page_source  # 得到页面element的html代码
        tree = etree.HTML(text)

        test1 = tree.xpath("//*[@id='today']/div[1]/div/div[1]/span/text()")[0]
        # test2 = tree.xpath("//*[@id='today']/div[1]/div/div[1]/a/text()")

        if (test1 == "相对湿度"):
            time = tree.xpath("//*[@id='today']/div[1]/div/p[1]/span/text()")[0]
            tem = tree.xpath("//*[@id='today']/div[1]/div/div[3]/span/text()")[0] + '℃'
            zs_h1 = tree.xpath("//*[@id='today']/div[1]/div/div[1]/span/text()")[0]
            zs_h2 = tree.xpath("//*[@id='today']/div[1]/div/div[1]/em/text()")[0]
            zs_h = zs_h1 + zs_h2

            zs_w1 = tree.xpath("//*[@id='today']/div[1]/div/div[2]/span/text()")[0]
            zs_w2 = tree.xpath("//*[@id='today']/div[1]/div/div[2]/em/text()")[0]
            zs_w = zs_w1 + zs_w2

            zs_pol = tree.xpath("//*[@id='today']/div[1]/div/div[5]/span/a/text()")[0]
        else:
            time = tree.xpath("//*[@id='today']/div[1]/div/p[1]/span/text()")[0]
            tem = tree.xpath("//*[@id='today']/div[1]/div/div[4]/span/text()")[0] + '℃'
            zs_h1 = tree.xpath("//*[@id='today']/div[1]/div/div[2]/span/text()")[0]
            zs_h2 = tree.xpath("//*[@id='today']/div[1]/div/div[2]/em/text()")[0]
            zs_h = zs_h1 + zs_h2

            zs_w1 = tree.xpath("//*[@id='today']/div[1]/div/div[3]/span/text()")[0]
            zs_w2 = tree.xpath("//*[@id='today']/div[1]/div/div[3]/em/text()")[0]
            zs_w = zs_w1 + zs_w2

            zs_pol = tree.xpath("//*[@id='today']/div[1]/div/div[6]/span/a/text()")[0]

        sql = "INSERT INTO test1(城市,时间实况, 温度,相对湿度,风向级数,空气质量) VALUES ('%s','%s', '%s', '%s', '%s', '%s')" % (
            city_name, time, tem, zs_h, zs_w, zs_pol)

        try:
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()

    files.close()
except:
    print("error")

print("success")

# print("时间实况：" + time)
# print("温度：" + tem)
# print("相对湿度：" + zs_h)
# print("风向级数：" + zs_w)
# print("空气质量：" + zs_pol)

"""
# second test
import requests
from lxml import etree
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options  # 不显示页面
import time

# 不显示浏览器使用的过程
opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
# -------------------------------------
web = Chrome(options=opt)  # 把参数设置到浏览器
url = "http://www.weather.com.cn/weather1d/101010100.shtml"

web.get(url)
text = web.page_source  # 得到页面element的html代码
tree = etree.HTML(text)

time = tree.xpath("//*[@id='today']/div[1]/div/p[1]/span/text()")[0]  # 18:25 实况
tem = tree.xpath("//*[@id='today']/div[1]/div/div[4]/span/text()")[0] + '℃'  # 8
# //*[@id="today"]/div[1]/div/div[2]/em
zs_h1 = tree.xpath("//*[@id='today']/div[1]/div/div[2]/span/text()")[0]  # 相对湿度
zs_h2 = tree.xpath("//*[@id='today']/div[1]/div/div[2]/em/text()")[0]
zs_h = zs_h1 + zs_h2

zs_w1 = tree.xpath("//*[@id='today']/div[1]/div/div[3]/span/text()")[0]  # 东北风
zs_w2 = tree.xpath("//*[@id='today']/div[1]/div/div[3]/em/text()")[0]
zs_w = zs_w1 + zs_w2

zs_pol = tree.xpath("//*[@id='today']/div[1]/div/div[6]/span/a/text()")[0]  # 66良

# print(time + '\n', tem + '\n', zs_w + '\n', zs_pol + '\n')
print("时间实况：" + time)
print("温度：" + tem)
# print("zs_h1：" + zs_h1)
# print("zs_h2：" + zs_h2)
print("相对湿度：" + zs_h)
# print("zs_w1：" + zs_w1)
# print("zs_w2：" + zs_w2)
print("风向级数：" + zs_w)
print("空气质量：" + zs_pol)
"""

"""
# first test
import requests
from lxml import etree
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options  # 不显示页面
import time

# 不显示浏览器使用的过程
opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
# -------------------------------------
web = Chrome(options=opt)  # 把参数设置到浏览器
url = "http://www.weather.com.cn/weather1d/101010100.shtml"

web.get(url)
text = web.page_source  # 得到页面element的html代码
tree = etree.HTML(text)

time = tree.xpath("//*[@id='today']/div[1]/div/p[1]/span/text()")[0]  # 18:25 实况
tem = tree.xpath("//*[@id='today']/div[1]/div/div[4]/span/text()")[0] + '℃'  # 8
# //*[@id='today']/div[1]/div/div[2]/em
zs_h1 = tree.xpath("//*[@id='today']/div[1]/div/div[2]/span/text()")[0]  # 相对湿度
zs_h2 = tree.xpath("//*[@id='today']/div[1]/div/div[2]/em/text()")[0]

# //*[@id='today']/div[1]/div/div[3]/em
zs_w1 = tree.xpath("//*[@id='today']/div[1]/div/div[3]/span/text()")[0]  # 东北风
zs_w2 = tree.xpath("//*[@id='today']/div[1]/div/div[3]/em/text()")[0]  # 东北风

zs_pol = tree.xpath("//*[@id='today']/div[1]/div/div[6]/span/a/text()")[0]  # 66良

print("time" + time)
print("tem" + tem)
print("zs_h1" + zs_h1)
print("zs_h2" + zs_h2)
print("zs_w1" + zs_w1)
print("zs_w2" + zs_w2)
print("zs_pol" + zs_pol)

"""
