'''
学习多线程
1.多线程
2.thread库没有守护线程，threading 模块支持守护线程

版本2.0没创建一个线程特别麻烦，进行线程优化
版本3.0 创建一个线程类
'''


from time import sleep,ctime
#导入线程类
import threading


class MyThraed(threading.Thread):
    '''
    创建线程
    '''

    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        #函数
        self.args = args
        #参数
        self.name = name

    def run(self):
        self.func(*self.args)
#这是一种特殊的语法，在函数定义中使用*args和**kwargs传递可变长参数
# 。*args用作传递非命名键值可变长参数列表（位置参数）;
# **kwargs用作传递键值可变长参数列表。

def super_player(file_,time):
    '''创建播放器'''
    for i in range(2):
        #range()生成可迭代的列表
        print('Start playing : %s！ %s'%(file_,ctime()))
        sleep(time)


#节目字典
list = {'爱情买卖':6,'阿凡达':5,'一条狗的人人生':4}

files = range(len(list))
#range()生成可迭代的列
#创建线程数组
threds = []

#创建线程
for file_,time in list.items():
    t = MyThraed(super_player,(file_,time),super_player.__name__)
    threds.append(t)

def main():
    '''
    主函数
    '''
    #启动进程
    for t in files:
        threds[t].start()
    for t in files:
        threds[t].join()

    print('end: %s '% ctime())

if __name__ == '__main__':

     main()