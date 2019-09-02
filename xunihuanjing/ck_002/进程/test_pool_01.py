'''
1,进程池的基本操作
'''

from multiprocessing import Pool
import time,os

def work1():
    for i in range(10):
        print('work1-------{}---{}'.format(i,os.getpid()))
        time.sleep(0.1)

def work2():
    for i in range(10):
        print('work2-------{}---{}'.format(i,os.getpid()))
        time.sleep(0.1)

def main():
    po = Pool(5) #创建一个进程池,池中有5个进程
    for i in range(10):  #依次从进程池中拿出进程,创建10个进程,实际每次最多获取5个,其他等待
          po.apply_async(work1)

    for i in range(10):  #依次从进程池中拿出进程,创建10个进程,实际每次最多获取5个,其他等待
          po.apply_async(work2)

    po.close()  #关闭进程池,进程池不在接收新的任务
    po.join()   #等待主进程执行

if __name__ == '__main__':
    main()