import urllib.request
import urllib.parse

url = 'https://www.baidu.com/s?wd='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

name = urllib.parse.quote('周杰伦')
url = url + name

request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器放松数据
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
