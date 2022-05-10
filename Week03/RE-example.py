import re
match=re.search(r'[1-9]\d{5}','BIT 100081') #搜索字符串匹配正则表达式的第一个位置，返回match对象
if match:
    print(match.group(0))
match=re.match(r'[1-9]\d{5}','BIT 100081') #从字符串的开始位置匹配正则表达式，返回match对象
if match:
    print(match.group(0)) #空函数不能调用方法，否则会报错
match=re.match(r'[1-9]\d{5}','100081 BIT')
if match:
    print(match.group(0))
ls=re.findall(r'[1-9]\d{5}','BIT100081 TSU100084') #搜索字符串，以列表类型返回全部能匹配的字串
print(ls)
ls=re.split(r'[1-9]\d{5}','BIT100081 TSU100084') #将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
print(ls) #匹配的部分被去掉，剩下的放进列表
ls=re.split(r'[1-9]\d{5}','BIT100081 TSU100084',maxsplit=1) #只分割一次
print(ls)
for m in re.finditer(r'[1-9]\d{5}','BIT100081 TSU100084'): #搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
    if m:
        print(m.group(0))
s=re.sub(r'[1-9]\d{5}',':zipcode','BIT100081 TSU100084') #在一个字符串中替换所有匹配正则表达式的字串，返回替换后的字串
print(s)

