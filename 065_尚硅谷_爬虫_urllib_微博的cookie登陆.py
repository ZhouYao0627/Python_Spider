# 适用的场景：数据采集的时候 需要绕过登陆 然后进入到某个页面
# 个人信息页面是utf-8  但是还报错了编码错误  因为并没有进入到个人信息页面 而是跳转到了登陆页面
# 那么登陆页面不是utf-8  所以报错

# 什么情况下访问不成功？
# 因为请求头的信息不够  所以访问不成功

import urllib.request

url = 'https://weibo.com/u/6074555957/home?wvr=5'

headers = {
    # ':authority': 'weibo.com',
    # ':method': 'GET',
    # ':path': '/u/6074555957/home?wvr=5',
    # ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 这条信息代表本地可以接收压缩格式的数据，而服务器在处理时就将大文件压缩再发回客户端，IE在接收完成后在本地对这个文件又进行了解压操作。
    # 出错的原因是因为你的程序没有解压这个文件，所以删掉这行就不会出现问题了(下行)
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # cookie中携带着你的登陆信息   如果有登陆之后的cookie  那么我们就可以携带着cookie进入到任何页面
    'cookie': 'SINAGLOBAL=6076728738163.202.1528984951994; SCF=An1oATRFbToJ-6Y8TpPePWEVyTCUyRRtXu6nXcbpKdR1Yy_g7u2VZ9I9Xotk8SPl1uztUEN2eKFsxTyv3pNL2T0.; UOR=,,www.google.com; login_sid_t=9979608ec9350ecdb548f894ab88eb95; cross_origin_proto=SSL; WBStorage=5fd44921|undefined; _s_tentry=www.google.com; wb_view_log=1536*8641.25; Apache=6265446552634.391.1635989796048; ULV=1635989796054:6:1:1:6265446552634.391.1635989796048:1629682933596; SUB=_2A25Mh0kpDeRhGeBO7FYU9SvFzjuIHXVv9T3hrDV8PUNbmtANLU7jkW9NRatatSEp4lMl3-bJHYTk9XlEhFk82N5y; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFOQY6AjyFzM2sei7gwCs-R5JpX5KzhUgL.Foq7S0BfSK-4SKM2dJLoIEXLxKBLBonL1-eLxK.LBKeL12-LxKqL1-eLB-2LxKqLB--L12zLxKnL122LBo2t; ALF=1667525879; SSOLoginState=1635989881; wvr=6; wb_view_log_6074555957=1536*8641.25; webim_unReadCount=%7B%22time%22%3A1635989882900%2C%22dm_pub_total%22%3A36%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A36%2C%22msgbox%22%3A0%7D',
    # referer  判断当前路径是不是由上一个路径进来的    一般情况下 是做图片防盗链
    'referer': 'https://weibo.com/login.php',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
}
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取响应的数据
content = response.read().decode('utf-8')

# 将数据保存到本地
with open('weibo.html', 'w', encoding='utf-8')as fp:
    fp.write(content)
