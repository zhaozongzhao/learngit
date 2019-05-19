
#yield可以用来为一个函数返回值塞数据
def addlist(list):
    for i in list:
        yield i+1

#yield 每次返回一个数据,int类型
list = [1,2,3,4,5]
for x in addlist(list):
    print(x)

#包含yield的函数

def h():
    print('studu yield')
    yield 5
    print('go on')

c = h()
d1 = next(c)
d2 = next(c)