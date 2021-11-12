# first test
import requests
from bs4 import BeautifulSoup

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


def parse_page(html, return_list):
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

        return_list.append([date, wea, lowtem, hightem, wind, level])


def print_res(return_list):
    tplt = '{0:<10}\t{1:{6}^10}\t{2:{6}^10}\t{3:{6}^10}\t{4:{6}^10}\t{5:{6}^10}'
    result_list_wt.append(tplt.format('日期', '天气', '最高温度', '最低温度', '风向', '风力等级', chr(12288)) + "\n")
    for i in return_list:
        result_list_wt.append(
            tplt.format(i[0], i[1], i[2], i[3], i[4], i[5], chr(12288)) + "\n")  # 宽度不够时采用中文空格填充，中文空格的编码为chr(12288)


def main():
    files = open('city_list.txt', 'r', encoding='utf-8')
    city_name_id = files.readlines()

    try:
        for line in city_name_id:
            city_name = line.split('-')[0].replace("\n", "")
            city_id = line.split('-')[1].replace("\n", "")
            # http://www.weather.com.cn/weather1d/101030100.shtml#input
            url = 'http://www.weather.com.cn/weather/' + city_id + '.shtml'

            city_china = "\n" + "城市名：" + city_name + "\n"
            result_list_wt.append(city_china)

            html = get_page(url)  # 获取网页数据

            wea_list = []
            parse_page(html, wea_list)  # 解析   ---> 出错

            print_res(wea_list)
        files.close()
    except:
        print("error1")

    # 将获取结果写入到文件内
    msgs = ''.join(result_list_wt)
    with open('weather.China_test.txt', 'w', encoding='utf-8') as fp:
        fp.write(msgs)


if __name__ == '__main__':
    main()
