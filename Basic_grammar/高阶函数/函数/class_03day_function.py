"""
函数

1，递归函数

2，纯函数

3，匿名函数

4，便函数

5，闭包

"""

import time


#####递归函数############
# 递归 阶乘
def jie_func(n):
    if n == 1:
        return 1  # 递归边界
    else:
        return n * jie_func(n - 1)


res = jie_func(3)
print(res)

# 缓存装饰器
from functools import lru_cache


@lru_cache(maxsize=128)
def function_999(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return function_999(n - 1) + function_999(n - 2) + function_999(n - 3)


print(function_999(100))


###########纯函数 ###############

def add(a, b):
    return a + b


"""

内置函数
"""


def sqbare(n):
    """
    计算平方根
    :param n:   计算的参数
    :return:
    """
    return n ** 2


num = map(sqbare, [1, 2, 3, 4])  # Python 2.x 返回列表。Python 3.x 返回迭代器。
print(type(num))
print(list(num))


def is_odd(n):
    """
    过滤出列表中的所有奇数
    :return: 
    """
    return n % 2 == 1


newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(newlist))

list1 = ['name', 'age', 'gender']
list2 = ['strrage', '17', '男']

num = zip(list1, list2)
print(list(num))

print("Loading", end="")
for i in range(20):
    print(".", end=" ")
    time.sleep(0.5)

"""
使用内置函数，将列表转为枚举
"""
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print(i, element)

"""
匿名函数

"""


def fun1(n):
    '''
    普通函数的写法
    '''
    return n * 2


(lambda n: n * 2)(4)  # 匿名函数的定义后可以直接调用

res = (lambda n: n * 2)(4)  # 匿名函数可以在函数定义后用变量接受保存，单是一般不这样做

h = filter((lambda x: x <= 5), [1, 22, 3, 4, 5, 6, 11, 44])
print(list(h))

"""
偏函数
"""
