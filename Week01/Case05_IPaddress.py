import requests
url="http://mip.chinaz.com/?query="
IPadd="27.38.193.29"
try:
    r=requests.get(url+IPadd)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.request.url)
    print(r.text[:1000])
except:
    print("爬取失败")
