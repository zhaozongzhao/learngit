import os
print('进程{}开始'.format(os.getpid()))

pid = os.fork()

if pid == 0:
    print('我是子进程{}，我的父进程是{}'.format(os.getpid(),os.getppid()))
else:
    print('过程{}开始……{}'.format(os.getpid(),pid))


from multiprocessing import Process

#子进程要执行代码
def run_proc(name):
    print('run child process {} {}'.format(name,os.getpid()))

if __name__ == '__main__':
    print('parent process {}'.format(os.getpid()))
    p = Process(target = run_proc,args = ('test',))
    print('child process will start')
    p.start()
    p.join()
    print('child process end')

#Pool
#如果要启动大量的子进程,可以用进程池的方式批量创建子进程
from multiprocessing import Pool
import time,random

def long_time_task(name):
    print('Run task {} {}'.format(name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task {} runs {} seconds'.format(name,end-start))


if __name__ == '__main__':
    print('Parent process {}'.format(os.getpid()))
    p =Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('walking for all subprocesses done...')
    p.close()
    p.join()
    print('all subprocesses done')
