import requests
from bs4 import BeautifulSoup
r=requests.get("http://python123.io/ws/demo.html")
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
print(soup.head)
print(soup.head.contents) #返回的是一个列表
print(soup.body.contents)
print(len(soup.body.contents))
print(soup.title.parent)
print(soup.html.parent)
for parent in soup.a.parents: #对a标签所有先辈名称遍历
    if parent is None: 
        print(parent)
    else:
        print(parent.name)
print(soup.a.next_sibling) #标签之间的navigablestring也构成一个节点
print(soup.a.next_sibling.next_sibling) #返回了另一个a标签
print(soup.a.previous_sibling) #返回了解释a标签之前的文本信息
print(soup.a.previous_sibling.previous_sibling) #返回为空

