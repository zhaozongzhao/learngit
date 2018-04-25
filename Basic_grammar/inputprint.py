s= 'Hello Word'
print(str(s))
print(repr(s))  #返回一个解释器易读的表达式
print(s)

print(repr(s).rjust(20),repr(s))#rjust ,可以将字符串靠右,并在左边填充空格



#str.format()基本使用方法
print('网址{},{}'.format('百度','www.baidu.com'))

#传入参数位置
print('网址{0},{1}'.format('百度','www.baidu.com'))

#使用关键字参数

print('网址{name},{url}'.format(url = 'www.baifu.com',name = '百度'))

#使用!a,!s(str),!r(reor)可以在格式话之前进行转化

print('网址{!s},{!r}'.format('百度','www.baidu.com'))

#传入字典
table = {'gle':1,'oob':2,'taobao':3}
print('gel:{0[gle]:d},oob:{0[oob]:d},taobao:{0[taobao]:d}'.format(table))