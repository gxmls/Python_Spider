import requests
from bs4 import BeautifulSoup
r=requests.get("http://python123.io/ws/demo.html")
demo=r.text
soup=BeautifulSoup(demo,"html.parser") #html.parser是解析器
print(soup.prettify())
print(soup.title)
tag=soup.a #只能返回第一个a标签的内容
print(type(tag)) #查看tag的类型，是bs.element.Tag
print(tag)
print(soup.a.name) #返回a标签的名字
print(soup.a.parent.name) #返回包含a标签的上一层标签名字
print(soup.a.parent.parent.name) #返回包含a标签的上一层标签的再上一层标签的名字
print(tag.attrs) #返回字典形式
print(type(tag.attrs)) #查看tag.attrs属性
print(tag.attrs['class']) #返回字典中class对应的值
print(soup.a.string) #返回<>之间的非属性字符串
print(soup.p.string) #返回p标签中b标签中的字符串，可跨多个标签
newsoup=BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>","html.parser")
'''
用<!-->表示注释的开始
'''
print(newsoup.b.string) #返回注释
print(type(newsoup.b.string)) #查看注释的类型
print(type(newsoup.p.string)) #p标签不是注释

