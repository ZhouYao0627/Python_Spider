import urllib.request
import urllib.error

# url = 'https://blog.csdn.net/sulixu/article/details/1198189491'

url = 'http://www.doudan1111.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

try:
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError:
    print('系统正在升级。。。')
except urllib.error.URLError:
    print('我都说了 系统正在升级。。。')
