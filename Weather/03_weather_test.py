import requests
import pymysql
from bs4 import BeautifulSoup

conn = pymysql.connect(user='root', password='123456', host='localhost', database='weather2', port=3306,
                       charset='utf8')
cursor = conn.cursor()


def get_temperature(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    }

    response = requests.get(url, headers=headers).content
    soup = BeautifulSoup(response, 'lxml')

    conmid2 = soup.find('div', 'conMidtab').findAll('div', 'conMidtab2')

    for info in conmid2:
        tr_list = info.find_all('tr')[2:]
        for index, tr in enumerate(tr_list):
            td_list = tr.find_all('td')
            if index == 0:
                city_name = td_list[1].text.replace('\n', '')
                wea = td_list[2].text.replace('\n', '')
                wind = td_list[3].text.replace('\n', '')
                maxtemp = td_list[4].text.replace('\n', '')
                mintemp = td_list[7].text.replace('\n', '')
            else:
                city_name = td_list[0].text.replace('\n', '')
                wea = td_list[1].text.replace('\n', '')
                wind = td_list[2].text.replace('\n', '')
                maxtemp = td_list[3].text.replace('\n', '')
                mintemp = td_list[6].text.replace('\n', '')

            sql = "INSERT INTO testw1(city, wea, wind, maxtemp, mintemp) VALUES ('%s', '%s', '%s', '%s', '%s')" % (
                city_name, wea, wind, maxtemp, mintemp)

            cursor.execute(sql)
            conn.commit()


if __name__ == '__main__':
    data = ['hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn']

    for i in range(len(data)):
        url = 'http://www.weather.com.cn/textFC/' + data[i] + '.shtml'
        get_temperature(url)

    print('success')
