import urllib.request

# url = 'https://dianying.taobao.com/cityAction.json?city=&_ksTS=1636165407257_48&jsoncallback=jsonp49&action=cityAction&n_s=new&event_submit_doLocate=true'
url = 'https://dianying.taobao.com/showAction.json?_ksTS=1636165407488_93&jsoncallback=jsonp94&action=showAction&n_s=new&event_submit_doGetSoon=true'

headers = {
    # ':authority': 'dianying.taobao.com',
    # ':method': 'GET',
    # ':path': '/showAction.json?_ksTS=1636165407488_93&jsoncallback=jsonp94&action=showAction&n_s=new&event_submit_doGetSoon=true',
    # ':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'enc=vL%2F%2BuzmMmHaosib4IwTFY2amkfaMIe%2BIJxbGeKApVwygxpMwJlYhXcQj0EoobZPD%2Fq4aqWFMZJ7PKJbGJTtQkg%3D%3D; t=96f940af8fd96a78f36dd600d0de78aa; cna=ZK0iGeZxh00CAd5eITkAVnnR; miid=388373035193258546; cookie2=1096b4daa49de9c58ccc0a47807fbae9; v=0; _tb_token_=7b377eaffe9e1; xlly_s=1; tb_city=110100; tb_cityName="sbG+qQ=="; tfstk=cRVOBAcUZMjgfPgLzRBhlVGdzY7hZv8tmFivMwQnzMxG_jAAiBNuwkTdCqorXwC..; l=eBgHiDBggzk9GuSdBOfZlurza77tdIRYjuPzaNbMiOCPOU5p5YU5W6C70tY9CnGVhsIJR3yi5VR8BeYBq_C-nxvTaxom4jHmn; isg=BPn5lbC9vG2gtVpe_ocZ4kjTCGXTBu248ZgI_xsudSCfohk0Y1b9iGf0JKZUIYXw',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# split切割
content = content.split('(')[1].split(')')[0]

with open('074_尚硅谷_爬虫_解析_jsonpath解析淘票票.json', 'w', encoding='utf-8')as fp:
    fp.write(content)

import json
import jsonpath

obj = json.load(open('074_尚硅谷_爬虫_解析_jsonpath解析淘票票.json', 'r', encoding='utf-8'))

city_list = jsonpath.jsonpath(obj, '$..director')

print(city_list)
