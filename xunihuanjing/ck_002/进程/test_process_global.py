
"""
1,进程间的通讯

"""
#用法1
from multiprocessing import Process,Lock,Queue #导入进程模块
# from queue import Queue
import os,time
qc = Queue()
for i in range(5):
    qc.put(i)

def work3(qc):
    while not qc.empty():
        print('进程{}获取值{}'.format(os.getpid(),qc.get()))


def work4(qc):
    while  not qc.empty():
        print('进程{}获取值{}'.format(os.getpid(), qc.get()))


meto = Lock()
#用法1
if __name__ == '__main__':

    p1 = Process(target=work3,args=(qc,))  #创建进程任务并将进程间传递的参数传入
    p2 = Process(target=work4,args=(qc,))  #创建进程任务并将进程间传递的参数传入
    p1.start() #启动进程任务
    p2.start() #启动进程任务
    p1.join() #等待子进程运行完成
    p2.join()
    print('___________结束————————————————————————')








