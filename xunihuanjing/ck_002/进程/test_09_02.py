"""
1,进程

"""
# 用法1
# from multiprocessing import Process #导入进程模块
# from time import sleep
#
# def work1():
#     for i in range(6):
#         print(F'{i}正在浇花')
#         sleep(0.5)
#
#
# def work2():
#     for i in range(6):
#         print(F'{i}正在打水')
#         sleep(0.5)
# #用法1
# if __name__ == '__main__':
#     p1 = Process(target=work1)  #创建进程任务
#     p2 = Process(target=work2)
#     p1.start() #启动进程任务
#     p2.start() #启动进程任务
#     p1.join() #等待子进程运行完成
#     p2.join()
#     print('___________结束————————————————————————')

# 用法2
from multiprocessing import Process, Lock
import time, os


class MyProcess(Process):
    def __init__(self, meto):
        super().__init__()
        self.meto = meto

    def run(self):  # 执行的方法
        meto.acquire()  # 上锁
        with open('test.txt', mode='a', encoding='utf-8')  as f:
            for i in range(5):
                # 获取进程id的两种方式一种self.pid 一种os.pid
                print('进程{}正在写入'.format(os.getpid()))
                print('进程{}正在写入'.format(self.pid))
                f.write('python/t')
                time.sleep(1)
        meto.release()  # 解锁


class MyProcess2(Process):
    def __init__(self, meto):
        super().__init__()
        self.meto = meto

    def run(self):  # 执行的方法
        meto.acquire()  # 上锁
        with open('test.txt', mode='a', encoding='utf-8')  as f:
            for i in range(5):
                print('进程{}正在写入'.format(self.pid))  # 获取进程id的两种方式一种self.pid 一种os.pid
                f.write('java\n')
                time.sleep(1)
        meto.release()  # 解锁


meto = Lock() #多进程公用外部资源需要加锁


def main():
    c1 = MyProcess(meto)
    c2 = MyProcess2(meto)
    c1.start()
    c2.start()
    c1.join()
    c2.join()
    # c1.terminate()  # 不管是否执行完成直接停止



if __name__ == '__main__':
    main()
