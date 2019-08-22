from threading import Thread
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

     def __init__(self,url):
         super().__init__()
         self.url = url

     def run(self):
         for i in  range(2):
             requests.get(self.url)
             print('{}次请求'.format(i))




@func2
def main():
    t_list = []
    for i  in range(2):
        t = Mythead('http://smart.sqbj.com/')
        t.start()
        t_list.append(t)

    #遍历所有线程对象,等待子线程执行完成
    for t in t_list:
        t.join()


if __name__ == '__main__':
    main()