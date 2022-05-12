import re

from numpy import mat
match=re.search(r'PY.*N','PYANBNCNDN') #以PY开头，以N结尾，中间可以有若干字符串
print(match.group(0)) #匹配结果有多种可能，最短是PYAN，最长是PYANBNCNDN，但是re默认贪婪匹配
match=re.search(r'PY.*?N','PYANBNCNDN') #加一个问号，就可以匹配出最短的字符串
print(match.group(0))
