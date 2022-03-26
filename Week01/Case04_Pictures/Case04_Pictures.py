import requests
import os
url="https://img.pconline.com.cn/images/upload/upc/tx/photoblog/1904/06/c1/140758045_1554520548648_mthumb.jpg"
root="E://Learning Python//Python-spider//Week01//Case04_Pictures//"
path=root+url.split('/')[-1] #获取文件名
try:
    if not os.path.exists(root): #判断根目录是否存在
        os.mkdir(root) #如果不存在创建根目录
    if not os.path.exists(path): #判断文件是否存在，如果不存在创建文件
        r=requests.get(url) 
        with open(path,'wb') as f: #打开文件，标识符f
            f.write(r.content) #将返回的对象写入文件
            f.close()
    else:
        print("文件已存在")
except:
    print("爬取失败")
