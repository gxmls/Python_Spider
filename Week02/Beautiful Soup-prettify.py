import requests
from bs4 import BeautifulSoup
r=requests.get("http://python123.io/ws/demo.html")
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
print(soup.prettify())
print(soup.a.prettify()) #python3.X默认是UTF-8编码，可以显示中文