import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

headers = {
    # 'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '135',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=BEBFCCACFA48E8484B795467244253DF; PSTM=1523796782; __yjs_duid=1_31c025bf0a4a8fc85ebcccf7a6afb1ee1620203165382; BAIDUID=4735D9F314AF06D8EC68DF3896805761:FG=1; BDSFRCVID_BFESS=ow8OJeC62i6yt6jHOanmhehHrxcAKe7TH6f3shc06_POBcQkV6hJEG0PbM8g0Kuba53NogKKL2OTHmIF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tJAD_I--JDP3jnFkM-n_bnIJMq7OetJXfKOfVp7F5l8-hRIC2J8-Mxkg-fTLaPQ3WTrO3hjc5C3xOKQIDnbs-TOBBn393tJI2aFqBpcN3KJmHlC9bT3v5tD_jHbw2-biW2tH2MbdalTP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhbLGe4bK-TrWja8H3e; H_WISE_SIDS=110085_127969_168389_175667_177371_177985_178384_178617_179433_180276_181126_181133_181135_181588_182000_182233_182529_182860_183031_183220_183330_183975_184009_184267_184319_184441_184793_184809_185029_185362_185517_185751_185879_186317_186412_186596_186644_186656_186659_186743_186830_186844_187019_187023_187042_187070_187121_187175_187190_187205_187287_187309_187390_187432_187532_187605_187669_187726_187816_187925_187928_187935_187963_187992_188041_188181_188425_188495_188731_188804_188832_188846; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID_BFESS=4735D9F314AF06D8EC68DF3896805761:FG=1; ZD_ENTRY=google; H_PS_PSSID=26350; delPer=0; PSINO=5; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDUSS=NkMmlNQVZlLXNGWU1hQlR4OVByQ1lIUjhVa2Nwall2d2VOT0lhalJ1UUVzYWxoRVFBQUFBJCQAAAAAAAAAAAEAAACYNf6DzNK087jpx7MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQkgmEEJIJhWG; BDUSS_BFESS=NkMmlNQVZlLXNGWU1hQlR4OVByQ1lIUjhVa2Nwall2d2VOT0lhalJ1UUVzYWxoRVFBQUFBJCQAAAAAAAAAAAEAAACYNf6DzNK087jpx7MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQkgmEEJIJhWG; BDRCVFR[hwy28rfDaDR]=mk3SLVN4HKm; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1635492270,1635927027,1635936952,1635936960; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1635936960; __yjs_st=2_ODA0Y2U5NTQ5M2FjNTU0MzRhZGU3NGFlMGU2ZDY5OGViMDdkOTViNjU1OWYxMmI0ZGU4YTQ0YWJhZmI4MjRkNTFiYjc2MDU3ZmQ3NDdjMDA3MDkyNjE2ZjQyOWQwM2UzNzAyNzU3ZWQ3M2ZiYTQzN2NmYjA2NDE1YTBlYzE0M2MzNWE2YWVjODQzY2VmYjM4ODk1YWY0YzA0N2U5NWYyY2QyYWIxY2Q3MjhhMjkzMTVhYTdkMmZmZGUzYWRmYmE4NDc2ZjA2NjdmZTc4YzQ3ZDYwYTliYWUzOWZlYTllM2NjN2RiOGQ1YTVhODU3OTIwN2Q5ZGQ1OGVmNWFjNjEwNV83X2EzMWNlYjQ5; ab_sr=1.0.1_MGQ5ZjFmN2IzNGE5NTBmMTY4OTBhODEzZGYzMTQ1ZjQ0NmJkODhmMzFjMDYxMTdkYmI3MWRiYjQ2YTZjZDBhMDQzOGE3ZDY3YjhkM2U1MDIwOTg3NmFhYzRmODM4NWIwM2M0NmE4NThjOWFhZTA3NzNjY2M0ODdiMGNjMWUwZTE5NGE5NjBmZWVlNWJmZTNmNzY2MmI0OWZjOTkwMjFiNTQyNDUwY2U0YTZhZWQ0NTcyMTkwYTBjMzI0Y2M0YWY1',
    # 'Host': 'fanyi.baidu.com',
    # 'Origin': 'https://fanyi.baidu.com',
    # 'Referer': 'https://fanyi.baidu.com/',
    # 'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    # 'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': '9bb7abd8abf29817905d2a4bb2a5ac1b',
    'domain': 'common',
}
# post???????????????  ?????????????????? ???????????????encode??????
data = urllib.parse.urlencode(data).encode('utf-8')

# ?????????????????????
request = urllib.request.Request(url=url, data=data, headers=headers)

# ???????????????????????????????????????
response = urllib.request.urlopen(request)

# ?????????????????????
content = response.read().decode('utf-8')

import json

obj = json.loads(content)
print(obj)
