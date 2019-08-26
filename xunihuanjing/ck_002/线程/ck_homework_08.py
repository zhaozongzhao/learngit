
"""
1、描述并发和并行的概念
   并发：当前任务数大于cpu核数,通过任务调度算法,实现多个任务一起执行(实际是快速切换执行)
   并行：当前任务数小于cpu核数在,每个任务单独执行

2、简单python线程的缺陷，以及适用场景
   由于python设计之初，没预料到多核cpu能够得到现在的发展，只考虑到了单核cpu。为了更好的实现多线程之间数据完整性与状态同步，
   于是设计出了一个全局解析器锁（GIL, global interpreter lock)。 GIL确保Python进程一次运行一个线程(其它线程处于等待I/O或者睡眠状态)
   无论当前cpu有多少核心。这就意味着Python虽然可以实现多线程，但是在任意时间点仅有一个核心在执行Python指令（即线程无法并行运算)，无法发挥
   现代多核cpu的性能。CPython解析只允许拥有GIL才能运行程序

   适用场景:
   1.存在大量的IO操作(网络，文件，输入，输出等操作时)可以节省时间


"""
#3、创建一个线程类，开启3个线程去请求，一个地址300次。
from threading import Thread,Lock
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


#定义线程类
class Mythead(Thread):

     def __init__(self,url,name):
         super().__init__()
         self.url = url
         self.name = name

     def run(self):
         for i in  range(101):
             meta.acquire()   #上锁
             requests.get(self.url)
             meta.release()   #解锁
             print('线程{},第{}次请求'.format(self.name,i))




@func2
def main():
    t_list = []
    for i  in range(3):
        t = Mythead('https://www.douban.com','线程{}'.format(i+1))
        t.start()
        t_list.append(t)

    #遍历所有线程对象,等待子线程执行完成
    for t in t_list:
        t.join()


# 通过多线程实现一个文件复制器，传入一个路径，通过os模块相关方法获取该目录下所有的文件名，然后开启多线程对每个文件进行复制

import os
import shutil



#返回文件夹下所有的文件地址
def copy_file(filepath):

    file_list = []
    for filename in os.listdir(filepath): #返回包含目录中文件名称的列表。
        res = os.path.join(filepath, filename) #拼接每一个文件的路径并以列表的形式返回
        file_list.append(res)

    return file_list


# 创建一把锁
meta =  Lock()
#定义线程类
class Mythead2(Thread):

     def __init__(self,filepath,newpath,name):
         super().__init__()
         self.filepath = filepath
         self.newpath = newpath
         self.name = name

     def run(self):
          meta.acquire()  # 上锁
          path = shutil.copy(self.filepath,self.newpath)
          meta.release()  # 解锁
          print('线程{}文件{}复制完成'.format(self.name,self.filepath))

filepath = 'F:\gitstorehouse\learngit\\xunihuanjing\class_ckj01'
newpath  = 'F:\\gitstorehouse\\learngit\\xunihuanjing\\ck_002\\线程\\student'

@func2
def main1():
    filepaths = copy_file(filepath)
    t_list = []
    n = 1
    for i  in filepaths:
         t = Mythead2(i,newpath,n)
         t.start()
         n +=1

    #遍历所有线程对象,等待子线程执行完成
    for t in t_list:
        t.join()





if __name__ == '__main__':
    # main()
    main1()



