#python中多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。

#Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦

# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，
# 所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于
# 多个线程同时改一个变量，把内容给改乱了。

import time,threading

#毛毛的银行存款
balance  = 0
lock = threading.Lock()

def change_it(n):
    #先存后取,结果应该为0
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i  in range(10000000):
        lock.acquire()  #先获取锁
        change_it(i)
        lock.release()  #运行结束,解锁

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)