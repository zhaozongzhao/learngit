'''
协程gevent IO操作会切换
'''
import gevent


def work1():  # 工作任务
    for i in range(10):
        print('work1----{}'.format(i))
        gevent.sleep(0.5)


def work2():
    for i in range(10):
        print('work2----{}'.format(i))
        gevent.sleep(0.5)


g1 = gevent.spawn(work1) #指定工作函数
g2 = gevent.spawn(work2) #指定工作函数
g1.join()    #等待协程执行完成再往下走
g2.join()
