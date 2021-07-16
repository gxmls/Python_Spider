import requests
r=requests.get('http://www.baidu.com') #必须有‘http://’开头，否则会出错
print(r.status_code) #200表示访问成功，404表示访问失败
print(r.text) #会显示乱码
print(r.encoding) #编码方式 ISO-8859-1
print(r.apparent_encoding) #编码方式utf-8
r.encoding='utf-8'
print(r.text) #指定utf-8编码后，可以显示中文
