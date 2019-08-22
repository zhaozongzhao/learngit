'''
1，命名元祖
2，列表推导式
3, 三目运算
4，字典推导式
'''
# from  collections import namedtuple
#
# studeng = namedtuple('studengt', ['name', 'age', 'gender'])
# print(type(studeng))     #判断类型是一个类
# s1 = studeng('小明', 18, '男')
# print(type(s1))          #返回一个类
# print(s1.name)   #通过对应的字段取值
# print(s1[0])     #通过下标取值

# '''
# 2，列表推导式
# 3, 三目运算
# '''
num = [i for i in range(100)]  # 列表推导式


# print(num)
# num = [i for i in range(0,100,20) if i % 2 == 0]  #组合列表推导式和三目运算
# print(num)

# """
# 生成器表达式
# """
# tu = (i for i in range(5))
#
def func():
      i =0
      while i < 10:
        print(f'函数{i}的数值')
        k = yield i
        if k is not None:
            i = k
        i +=1

res = func()
print(next(res))
print(res.send(4))
# print(res)
# print(next(tu))
# print(next(res))
# print(next(tu))
# print(next(res))

#
# iter = iter(num)
# print(tu)
# print(iter)
