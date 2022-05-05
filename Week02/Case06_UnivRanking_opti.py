import bs4
import requests
from bs4 import BeautifulSoup

def getHTMLText(url): #获取url信息
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "" #如果爬取失败返回空字符串

def fillUnivList(html): #提取关键数据并放入列表中
    ulist=[]
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children: #所有大学信息存在tbody标签中，每个大学信息存于tr中
        if isinstance(tr,bs4.element.Tag): #过滤掉非Tag类型
            tds=tr.find_all('td') #对tr标签中的td做查询
            ranking=tds[0].string
            cnName=tds[1].find("a","name-cn").string #a标签中存放大学名称
            score=tds[4].string #第四个td标签才是存放评分的
            ulist.append([ranking.strip("\n "),cnName.strip("\n "),score.strip("\n ")]) #这里要注意用[]，并且清除空格和换行
    return ulist

def printUnivList(ulist,num): #将ulist信息打印出来，num表示多少个元素
    tplt="{0:^10}\t{1:{3}^10}\t{2:^11}"
    print(tplt.format("排名","学校名称","总分",chr(12288))) #chr(12288)用中文字符对齐解决中文排版问题
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288))) 

def main():
    url="https://www.shanghairanking.cn/rankings/bcur/2022"
    html=getHTMLText(url)
    ulist=fillUnivList(html)
    printUnivList(ulist,20) #打印排名前20的大学信息

main()

