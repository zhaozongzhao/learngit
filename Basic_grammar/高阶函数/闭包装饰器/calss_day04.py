"""
闭包：
1.函数中嵌套一个函数
2.外层函数的返回值是内层函数的函数名
3.内层嵌套函数对外层作用域有一个非全局作用域发的引用

"""


def func():
    num = 999

    def wrapper():
        print(num)

    return wrapper


res = func()
num = 1000
res()

"""
装饰器
"""
from ddt import ddt

# 普通装饰器

def decorator(func):
    def wrapper():
        func()

    return wrapper


@decorator  # @的作用等价于 在函数定义后执行 fun1 = decorator(fun1)
def fun1():
    print("这是原函数的功能")


fun1()
