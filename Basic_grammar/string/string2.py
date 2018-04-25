#python字符串内建函数
str = 'hello'
print(str.capitalize())  #将字符串的第一个字母变成大写

print(str.center(20,'*')) #返回一个原字符串居中,使用元素填充,默认填充字符是空格

print(str.count('o')) #查询字符在字符串中出现的次数

print(str.find('h'))   # 查询字符串中是否包含元素

name = ['adam', 'LISA', 'barT']


#map函数使用
def normailze(x):
    str = x.capitalize()
    return str

h = list(map(normailze,name))
print(h)

#reduce函数使用

def prod(x,y):
    return x*y



