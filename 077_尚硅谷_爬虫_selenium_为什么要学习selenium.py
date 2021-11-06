import urllib.request

url = 'https://www.jd.com/'

request = urllib.request.Request(url)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
