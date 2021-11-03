import urllib.request
import urllib.parse

base_url = 'https://www.baidu.com/s?'

data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}

new_data = urllib.parse.urlencode(data)

new_url = base_url + new_data

handers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

request = urllib.request.Request(url=new_url, headers=handers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
