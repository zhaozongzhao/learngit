"""
一、队列和线程完成下面要求
1、用一个队列来存储商品
2、创建一个专门生产商品的线程类，当商品数量少于50时，开始生产商品，每次生产200个商品，没生产完一轮 暂停1秒
3、创建一个专门消费商品的线程类，当商品数量大于10时就开始消费，,循环消费，每次消费3个。当商品实例少于10的时候，暂停2秒
 4、# 创建一个线程生产商品
 5个线程消费商品
二、多线程和多进程比较
用昨天三个线程发300个请求  和三个进程发300个请求做比较，看那个速度更快
"""
# 第一题"：
from queue import Queue
from threading import Thread
import time

cq = Queue()


# 生产商品
class Mythread1(Thread):
    def run(self):
        i = 1
        while True:
            if cq.qsize() <= 50:
                print('商品数{}小于50 开始生产'.format(cq.qsize()))
                while i <= 200:
                    cq.put(i)
                    print('生产第{}件商品'.format(i))
                    i += 1
                i = 0
                print('生产完一轮暂停1秒')
                time.sleep(1)
            else:
                print('商品数{}大于50'.format(cq.qsize()))


# 消费商品
class Mythread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name


    def run(self):
        while True:
            if cq.qsize() >= 10:
                while True:
                    for i in range(3):
                        h = cq.get()
                        print('线程{}消费商品{}'.format(self.name,h))
                    if cq.qsize() <= 10:
                        print('商品数量{}'.format(cq.qsize()) + '暂停3秒')
                        time.sleep(3)

def cqmain():

    th = Mythread1()
    th.start()
    th1 = []
    for t  in range(5):
          h = Mythread(t)
          h.start()
          th1.append(h)
    for t in th1:
         t.join()
    th.join()





# 第二题：
from threading import Thread, Lock
import time
import requests


def func2(func):
    """
    装饰器:计算运行时间
    """
    print('运行装饰器')

    def wrapper():
        stime = time.time()  # 获取开始运行时间
        func()
        etime = time.time()  # 获取结束时间
        print('程序运行时间{}秒'.format(etime - stime))

    return wrapper
meta = Lock()
# 线程类
class Mythead(Thread):
    def __init__(self, url, name):
        super().__init__()
        self.url = url
        self.name = name

    def run(self):
        for i in range(100):
            meta.acquire()  # 上锁
            requests.get(self.url)
            meta.release()  # 解锁
            print('线程{},第{}次请求'.format(self.name, i))


@func2
def main():
    t_list = []
    for i in range(3):
        t = Mythead('https://www.douban.com', '线程{}'.format(i + 1))
        t.start()
        t_list.append(t)

    # 遍历所有线程对象,等待子线程执行完成
    for t in t_list:
        t.join()


# 多进程
from multiprocessing import Process, Lock

meta2 = Lock()


class MyProcess(Process):
    def __init__(self, url, name):
        super().__init__()
        self.url = url
        self.name = name

    def run(self):
        for i in range(100):
            requests.get(self.url)
            print('线程{},第{}次请求'.format(self.name, i))


@func2
def main2():
    t_list = []
    for i in range(3):
        t = MyProcess('https://www.douban.com', '进程{}'.format(i + 1))
        t.start()
        t_list.append(t)

    # 遍历所有线程对象,等待子线程执行完成
    for t in t_list:
        t.join()


if __name__ == '__main__':
    cqmain()
    main() #线程运行
    main2() #进程运行
