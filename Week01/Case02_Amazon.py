import requests
url="https://www.amazon.cn/dp/B087LZRDHR/ref=lp_144180071_1_3"
try:
    kv={"user-agent":"Mozilla/5.0"} #重新定义user-agent，模拟一个浏览器
    r=requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")
