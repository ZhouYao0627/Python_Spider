# (1) 请求对象的定制
# （2）获取网页的源码
# （3）下载

# 需求 下载的前十页的图片
# https://sc.chinaz.com/tupian/qinglvtupian.html     1
# https://sc.chinaz.com/tupian/qinglvtupian_2.html   2
# https://sc.chinaz.com/tupian/qinglvtupian_3.html   3
# ...
# https://sc.chinaz.com/tupian/qinglvtupian_page.html

import urllib.request
from lxml import etree


def create_request(page):
    if (page == 1):
        url = 'https://sc.chinaz.com/tupian/qinglvtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/qinglvtupian_' + str(page) + '.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
    }

    request = urllib.request.Request(url=url, headers=headers)

    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def down_load(content):
    tree = etree.HTML(content)

    name_list = tree.xpath('//div[@id="container"]//a/img/@alt')
    src_list = tree.xpath('//div[@id="container"]//a/img/@src2')

    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = "https:" + src

        urllib.request.urlretrieve(url, filename='./loveImg/' + name + '.jpg')


if __name__ == '__main__':
    start_page = int(input("请输入初始页码"))
    end_page = int(input("请输入结束页码"))

    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        down_load(content)
