
"""
1,进程

"""
#用法1
from multiprocessing import Process,Lock,Value #导入进程模块
from time import sleep
number = 0
def work1(meto, number):
    number = int(number)
    for i in range(100000):
        meto.acquire()
        number +=1
        meto.release()
    print(number)

def work2(meto,number):
    number = int(number)
    for i in range(100000):
        meto.acquire()
        number += 1
        meto.release()
    print(number)

meto = Lock()
#用法1
if __name__ == '__main__':

    p1 = Process(target=work1,args=(meto, number))  #创建进程任务
    p2 = Process(target=work2,args=(meto, number))
    p1.start() #启动进程任务
    p2.start() #启动进程任务
    p1.join() #等待子进程运行完成
    p2.join()
    print(number)
    print('___________结束————————————————————————')








