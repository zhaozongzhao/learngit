import re

#re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。

print(re.match('www','www.runoob.com').span())#在开始位置匹配
print(re.match('com','www.baidu.com'))   #不在开始部分匹配


print(re.search('www','www.runoob.com').span())  #在起始位置匹配
print(re.search('com','www.runoob.com').span())  #不在起始位置匹配


#替换字符串
phone = '2004-959-559 #这是一个手机号码'
num = re.sub('#.*$','',phone)
print('电话号码:',phone)

#移除非数字
num = re.sub('\D','',phone)
print(num)


path = re.compile('www')
m = path.match('www.baidu.com').span()
print(m)


#查找字符串
path = re.compile('\D')
m = path.findall('www.baidu6712786e21786123768.com')
print(m)

#查找字符串

it = re.finditer(r"\d+","12a32bc43jf3")
for match in it:
  print (match.group() )