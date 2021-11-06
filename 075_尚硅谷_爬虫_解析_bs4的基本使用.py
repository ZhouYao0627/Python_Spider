from bs4 import BeautifulSoup

# 通过解析本地文件 来将bs4的基础语法进行讲解
# 默认打开的文件的编码格式是gbk 所以在打开文件的时候需要指定编码
soup = BeautifulSoup(open('075_尚硅谷_爬虫_解析_bs4的基本使用.html', encoding='utf-8'), 'lxml')

# 根据标签名查找节点
# print(soup.a)  # 找到的是第一个符合条件的数据
# print(soup.a.attrs)  # 获取标签的属性和属性值

# bs4的一些函数
# （1）find
# print(soup.find('a'))  # 返回的是第一个符合条件的数据
# print(soup.find('a',title="a2"))  # 根据title的值来找到对应的标签对象
# print(soup.find('a',class_="a1"))  # 根据class的值来找到对应的标签对象  注意的是class需要添加下划线

# （2）find_all  返回的是一个列表
# print(soup.find_all('a'))  # 返回了所有的a标签
# print(soup.find_all(['a','span']))  # 如果想获取的是多个标签的数据 那么需要在find_all的参数中添加的是列表的数据
# print(soup.find_all('li',limit=2))  # limit的作用是查找前几个数据

# （3）select（推荐）
# print(soup.select('a'))  # select方法返回的是一个列表  并且会返回多个数据
# print(soup.select('.a1'))  # 可以通过.代表class  我们把这种操作叫做类选择器
# print(soup.select('#l1'))


# 属性选择器---通过属性来寻找对应的标签
# print(soup.select('li[id]'))  # 查找到li标签中有id的标签
# print(soup.select('li[id="l2"]'))  # 查找到li标签中id为l2的标签


# 层级选择器
#  后代选择器
# print(soup.select('div li'))  # 找到的是div下面的li
#  子代选择器
#  注意：很多的计算机编程语言中 如果不加空格不会输出内容  但是在bs4中不会报错，会显示内容
# print(soup.select('div > ul > li'))  # 某标签的第一级子标签

# print(soup.select('a,li'))  # 找到a标签和li标签的所有的对象

# 节点信息
#   1.获取节点内容：适用于标签中嵌套标签的结构
# obj = soup.select('#d1')[0]
# 如果标签对象中 只有内容 那么string和get_text()都可以使用
# 如果标签对象中 除了内容还有标签 那么string就获取不到数据 而get_text()是可以获取数据
# 我们一般情况下  推荐使用get_text()
# print(obj.string)
# print(obj.get_text())

#  2.节点的属性
# obj = soup.select('#p1')[0]
# print(obj.name)  # name是标签的名字
# print(obj.attrs)  # 将属性值作为一个字典返回

#  3.获取节点的属性
obj = soup.select('#p1')[0]

print(obj.attrs.get('class'))
print(obj.get('class'))
print(obj['class'])
