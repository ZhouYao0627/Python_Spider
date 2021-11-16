# 这是将未来七天的天气信息给爬取下来
import requests
from bs4 import BeautifulSoup
import re  # re --- 正则表达式操作

result_list_wt = []


# 获取网页内容
# 通用代码框架
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


# 解析网页内容，得到数据
def parse_page(html, return_list):
    soup = BeautifulSoup(html, 'html.parser')
    day_list = soup.find('ul', 't clearfix').find_all('li')
    for day in day_list:
        date = day.find('h1').get_text()
        wea = day.find('p', 'wea').get_text()
        if day.find('p', 'tem').find('span'):
            hightem = day.find('p', 'tem').find('span').get_text()
        else:
            hightem = ''
        lowtem = day.find('p', 'tem').find('i').get_text()

        win = re.findall('(?<= title=").*?(?=")', str(day.find('p', 'win').find('em')))
        wind = '-'.join(win)

        level = day.find('p', 'win').find('i').get_text()
        return_list.append([date, wea, lowtem, hightem, wind, level])


def print_res(return_list):
    # https://zhidao.baidu.com/question/368788419926022804.html
    tplt = '{0:<10}\t{1:^10}\t{2:^10}\t{3:{6}^10}\t{4:{6}^10}\t{5:{6}^5}'
    result_list_wt.append(tplt.format('日期', '天气', '最低温', '最高温', '风向', '风力', chr(12288)) + "\n")
    for i in return_list:  # https://blog.csdn.net/Heart_for_Ling/article/details/109247500
        result_list_wt.append(tplt.format(i[0], i[1], i[2], i[3], i[4], i[5], chr(12288)) + "\n")  # 宽度不够时采用中文空格填充，中文空格的编码为chr(12288)


def main():
    # 城市-城市码txt
    files = open('city_list.txt', "r", encoding='utf-8')
    city_name_id = files.readlines()
    try:
        # 获取txt-list
        for line in city_name_id:
            name_id = line.split('-')[1].replace("\n", "")
            url = 'http://www.weather.com.cn/weather/' + name_id + '.shtml'
            city_name = line.split('-')[0].replace("\n", "")
            city_china = "\n" + "城市名 : " + city_name + "\n"
            result_list_wt.append(city_china)

            html = get_page(url)  # 获取网页内容

            wea_list = []
            parse_page(html, wea_list)  # 解析网页内容，得到数据

            print_res(wea_list)
        files.close()
    except:
        print("error")

    # 将获取结果写入到文件内
    msgs = ''.join(result_list_wt)
    # print(msgs)
    with open('weather.China.txt', "w+") as file:
        file.write(msgs)


if __name__ == '__main__':
    main()
