# 自己的尝试
from bs4 import BeautifulSoup
import requests
import pymysql

# 打开数据库连接，并使用cursor()建立一个游标对象
conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='weather1', port=3306, charset='utf8')

cursor = conn.cursor()


# 创建request对象，指定url和请求头(user-agent),目的是为了更真实的模拟浏览器
def get_temperature(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    }  # 设置头文件信息

    response = requests.get(url, headers=headers).content  # 提交requests.get请求，传递url和headers
    soup = BeautifulSoup(response, "lxml")  # 用Beautifulsoup 进行解析

    div_list = soup.find('div', class_='curve_livezs').find_all('div')

    time_list = div_list[0].find_all('em')
    time = []
    for i in time_list:
        time.append(i.text.replace('\n', ''))

    tem_list = div_list[0].find_all('em')
    tem = []
    for i in tem_list:
        tem.append(i.text.replace('\n', ''))

    winf_list = div_list[0].find_all('em')
    winf = []
    for i in winf_list:
        winf.append(i.text.replace('\n', ''))

    winl_list = div_list[0].find_all('em')
    winl = []
    for i in winl_list:
        winl.append(i.text.replace('\n', ''))

    print(time, tem, winf, winl)

    sql = "INSERT INTO testweather(time1, tem, winf, winl) VALUES ('%s', '%s', '%s', %s)" % (time, tem, winf, winl)

    cursor.execute(sql)


if __name__ == '__main__':
    # for i in range(7):
    # data = [101020100, 101190401, 101190201, 101190101, 101190301, 101190203, 101190601, 101191101, 101210101,
    #         101210401]
    url = 'http://www.weather.com.cn/weather/101190101.shtml'
    # url = 'http://www.weather.com.cn/weather/' + str(data[i]) + '.shtml'
    get_temperature(url)

    # 提交
conn.commit()
