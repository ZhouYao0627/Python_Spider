import requests

url = 'http://www.weather.com.cn/weather/101190201.shtml'

headers = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'
}

# url:请求资源路径，params:参数，kwargs:字典
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'

content = response.text

# print(content)

# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(content, 'lxml')
#
# # //*[@id="today"]/script/text()
# # //div[@class='today clearfix']/script
# name_list = soup.select('div[class="today clearfix"] script')
#
# for name in name_list:
#     print(name.get_text())

from lxml import etree

# 解析服务器响应的文件
tree = etree.HTML(content)

# 获取想要的数据  xpath的返回值是一个列表类型的数据
result = tree.xpath("//*[@id='today']/script/text()")

for value in result:
    print(value.text)
    # with open('05_w.txt', 'w', encoding='utf-8')as fp:
    #     fp.write(result)

