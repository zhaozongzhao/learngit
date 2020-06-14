"""
命名元祖
下表操作与命名元祖相比：
下标操作通常会让代码表意不清晰，并且非常依赖记录的结构，即很依赖索引数值，添加了新的列的时候你的代码可能就会出错了，而且使得你的代码难以阅读

"""

from collections import namedtuple

studeng = namedtuple('studengt', ['name', 'age', 'gender'])
print(type(studeng))  # 判断类型是一个类
s1 = studeng('小明', 18, '男')
print(type(s1))  # 返回一个类
print(s1.name)  # 通过对应的字段取值
print(s1[0])  # 通过下标取值
