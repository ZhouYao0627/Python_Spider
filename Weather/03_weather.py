# 爬取中国所有城市的天气信息
# 导入模块
from bs4 import BeautifulSoup
import requests
import pymysql

# 打开数据库连接，并使用cursor()建立一个游标对象
conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='weather2', port=3306, charset='utf8')

cursor = conn.cursor()


# 创建request对象，指定url和请求头(user-agent),目的是为了更真实的模拟浏览器
def get_temperature(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    }  # 设置头文件信息

    response = requests.get(url, headers=headers).content  # 提交requests.get请求，传递url和headers
    soup = BeautifulSoup(response, "lxml")  # 用Beautifulsoup 进行解析

    conmid = soup.find('div', class_='conMidtab')
    conmid2 = conmid.findAll('div', class_='conMidtab2')

    for info in conmid2:
        tr_list = info.find_all('tr')[2:]  # 使用切片取到第三个tr标签
        for index, tr in enumerate(tr_list):  # enumerate可以返回元素的位置及内容
            td_list = tr.find_all('td')
            if index == 0:
                province_name = td_list[0].text.replace('\n', '')  # 取每个标签的text信息，并使用replace()函数将换行符删除
                city_name = td_list[1].text.replace('\n', '')
                weather = td_list[5].text.replace('\n', '')
                wind = td_list[6].text.replace('\n', '')
                max = td_list[4].text.replace('\n', '')
                min = td_list[7].text.replace('\n', '')
                print(province_name)
            else:
                city_name = td_list[0].text.replace('\n', '')
                weather = td_list[4].text.replace('\n', '')
                wind = td_list[5].text.replace('\n', '')
                max = td_list[3].text.replace('\n', '')
                min = td_list[6].text.replace('\n', '')

            print(city_name, weather, wind, max, min)

            sql = "INSERT INTO weather1(city, weather, wind, max, min) VALUES ('%s', '%s', '%s', %s, %s)" % (city_name, weather, wind, max, min)
            cursor.execute(sql)


if __name__ == '__main__':
    # 方法一
    # urls = ['http://www.weather.com.cn/textFC/hb.shtml',
    #         'http://www.weather.com.cn/textFC/db.shtml',
    #         'http://www.weather.com.cn/textFC/hd.shtml',
    #         'http://www.weather.com.cn/textFC/hz.shtml',
    #         'http://www.weather.com.cn/textFC/hn.shtml',
    #         'http://www.weather.com.cn/textFC/xb.shtml',
    #         'http://www.weather.com.cn/textFC/xn.shtml']
    #
    # for url in urls:
    #     get_temperature(url)

    # 方法二
    for i in range(7):
        data = ['hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn']
        url = 'http://www.weather.com.cn/textFC/' + data[i] + '.shtml'
        get_temperature(url)

    # 提交
    conn.commit()
