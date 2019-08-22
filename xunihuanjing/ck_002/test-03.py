# # 递归函数
#
# def func(n):
#     if n == 1: # 递归边界
#         return
#     print(n)
#     func(n-1)
#uoji
#
# #累加操作
# def func_add(n):
#     #判断n是否等于1
#     if n ==1:
#         return 1
#     else: #
#        return  func_add(n-1) + n
#
#
# #获取最大递归次数
# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(5000)
# print(sys.getrecursionlimit())
#
# #缓存装饰器
# from functools import lru_cache
#
# @lru_cache(maxsize=128)
# def func_add1(n):
#     #判断n是否等于1
#     if n ==1:
#         return 1
#     else: #
#        return  func_add(n-1) + n
# print(func_add1(10000))

h =2
print((lambda  x:x*2)(2))
print((lambda  x:x*2))
#偏函数
# from functools import partial
# def func11(a,b,c):
#      print(a)
#      print(b)
#      print(c)
#
# func11(11,22,333)
#
#
# func11_cp = partial(func11,a=11,c=22)
# print(func11_cp(b=33))


# lists = [i * 2 for i in range(5)]
# print('\n下面是使用while模拟for...in...的输出')
# iterator_ = iter(lists)
# while True:
#     try:
#         print(next(iterator_), end='')
#     except StopIteration as ret:
#         # print(ret)
#         break

def func():
    a=100
    def inter():
        print(a)
    return inter

a = func()
a()