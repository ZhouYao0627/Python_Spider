from selenium import webdriver
import time

# 创建浏览器对象
path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

# url
url = 'https://www.baidu.com'
browser.get(url)

time.sleep(2)  # 休眠2秒
input = browser.find_element_by_id('kw')  # 获取文本框的对象
input.send_keys('周杰伦')  # 在文本框中输入周杰伦

time.sleep(2)  # 休眠2秒
button = browser.find_element_by_id('su')  # 获取百度一下的按钮
button.click()  # 点击按钮

time.sleep(2)  # 休眠2秒
js_bottom = 'document.documentElement.scrollTop=100000'  # 滑到底部
browser.execute_script(js_bottom)

time.sleep(2)  # 休眠2秒
next = browser.find_element_by_xpath('//a[@class="n"]')  # 获取下一页的按钮
next.click()  # 点击下一页

time.sleep(2)  # 休眠2秒
browser.back()  # 回到上一页

time.sleep(2)  # 休眠2秒
browser.forward()  # 回去

time.sleep(3)  # 休眠3秒
browser.quit()  # 退出
