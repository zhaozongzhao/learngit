'''
1,进程池的基本操作\
2,进程池的通讯,队列
'''

from multiprocessing import Pool,Manager
import time,os

def work1(q):
    for i in range(10):
        print('work1-------{}---{}'.format(i,os.getpid()))
        q.put(1)

        time.sleep(0.1)

def work2(q):
    for i in range(10):
        print('work2-------{}---{}'.format(i,os.getpid()))
        time.sleep(0.1)
        print('获取队列的值',q.get())

def main():

    q1 =Manager().Queue()

    po = Pool(5) #创建一个进程池,池中有5个进程
    for i in range(10):  #依次从进程池中拿出进程,创建10个进程,实际每次最多获取5个,其他等待
          po.apply_async(work1,(q1,))

    for i in range(10):  #依次从进程池中拿出进程,创建10个进程,实际每次最多获取5个,其他等待
          po.apply_async(work2,(q1,))

    po.close()  #关闭进程池,进程池不在接收新的任务
    po.join()   #等待主进程执行

if __name__ == '__main__':
    main()