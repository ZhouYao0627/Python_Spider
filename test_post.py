import urllib.request
import urllib.parse
import json

url = 'https://fanyi.baidu.com/sug'

data = {
    'kw': 'spider'
}

data = urllib.parse.urlencode(data).encode('utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

request = urllib.request.Request(url=url, data=data, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

obj = json.loads(content)
print(obj)


