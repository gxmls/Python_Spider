import string
import requests
import re #正则表达式
from bs4 import BeautifulSoup
r=requests.get("http://python123.io/ws/demo.html")
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))
print(soup.find_all('a')) #检索全部a标签
print(soup.find_all(['a','b'])) #用列表
for tag in soup.find_all(True):#检索所有标签
    print(tag.name) 
for tag in soup.find_all(re.compile('b')): #以b开头的所有的信息，作为查找的要素
    print(tag.name)
print(soup.find_all('p','course')) #p标签中带有course信息的内容
print(soup.find_all(id='link1')) #直接对属性作为约定
print(soup.find_all(id='link')) #返回空列表，所以约定属性的时候必须精确约定
print(soup.find_all(id=re.compile('link'))) #用正则表达式，就可以给出部分信息
print(soup.find_all('a',recursive=False)) #儿子节点层面没有a标签
print(soup.find_all(string='Basic Python')) #返回列表，要精确输入要检索的字符串
print(soup.find_all(string=re.compile('python'))) #就可以返回所有包含python的字符串

