import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器访问服务器
# response = urllib.request.urlopen(request)

proxies = {
    'http': '118.24.219.151:16817'
}
# handler  build_opener  open
handler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(handler)

response = opener.open(request)

# 获取响应的信息
content = response.read().decode('utf-8')

# 保存
with open('daili.html', 'w', encoding='utf-8')as fp:
    fp.write(content)
