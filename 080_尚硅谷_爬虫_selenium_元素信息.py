from selenium import webdriver

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

url = 'http://www.baidu.com'
browser.get(url)

input = browser.find_element_by_id('su')

print(input.get_attribute('class'))  # 获取标签的属性
print(input.tag_name)  # 获取标签的名字

a = browser.find_element_by_link_text('新闻')  # 获取元素文本
print(a.text)
