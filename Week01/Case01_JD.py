import requests
url="https://item.jd.com/100015470570.html"

try:
    headers = {"User-Agent":"Chrome/80.0.3987.163","cookie": "自己浏览器的cookie信息"}
    '''
    因为京东啊，亚马逊都有反爬，所以要加入头部信息
    查询cookie方法：在对应网页按f12,然后在控制台输入document.cookie,回车就可
    '''
    r=requests.get(url,headers=headers)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:1001])
except:
    print("爬取失败")
