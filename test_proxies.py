import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)

proxies = {
    'http': '118.24.219.151:16817'
}

handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(headers)
response = opener.open(request)

content = response.read().decode('utf-8')
print(content)

with open('daili.html', 'w', encoding='utf-8')as fp:
    fp.write(content)
