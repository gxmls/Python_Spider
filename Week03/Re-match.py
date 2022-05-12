import re
match=re.search(r'[1-9]\d{5}','BIT 100081')
if match:
    print(match.group(0))
print(type(match)) 
m=re.search(r'[1-9]\d{5}','BIT100081 TSU100084')
print(m.string) #待匹配的文本
print(m.re) #匹配时使用的pattern对象（正则表达式），带compile标识的
print(m.pos) #正则表达式搜索文本的开始位置
print(m.endpos) #正则表达式搜索文本的结束位置
print(m.group(0)) #获得匹配后的字符串（返回第一次匹配的结果）
print(m.start()) #匹配字符串在原始字符串的开始位置
print(m.end()) #匹配字符串在原始字符串的结束位置
print(m.span()) #返回(.start(),.end())