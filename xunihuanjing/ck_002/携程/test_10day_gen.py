'''
1,协程的实现原理,底层通过 yield 实现
'''

def work1(): #工作任务
    for i in range(10):
        print('work1----{}'.format(i))
        yield i

def work2():
    for i in range(10):
        print('work2----{}'.format(i))
        yield i

def work3():
    for i in range(10):
        print('work3----{}'.format(i))
        yield i


g1 = work1()
g2 = work2()
g3 = work3()

while True: #循环调用生成器实现任务切换
    try:
        print(next(g1))
        print(next(g2))
        print(next(g3))
    except StopIteration :
        pass
        break