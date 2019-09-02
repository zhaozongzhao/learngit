'''
1,协程gevent IO操作会切换
2,猴子补丁,实现完全自动切换  monkey 不建议使用会修改好多操作
'''
import gevent,time
from gevent import monkey


monkey.patch_all()  #对所有模块打补丁



def work1():  # 工作任务
    for i in range(10):
        print('work1----{}'.format(i))
        time.sleep(0.5)          #打补丁后遇见普通的io操作就会切换
        # gevent.sleep(0.5)      #检测存在IO操作会自动切换已经准备好的协程中


def work2():
    for i in range(10):
        print('work2----{}'.format(i))
        time.sleep(0.5)
        # gevent.sleep(0.5)     #检测存在IO操作会自动切换已经准备好的协程中


g1 = gevent.spawn(work1) #指定工作函数
g2 = gevent.spawn(work2) #指定工作函数
g1.join()    #主协程等待子协程执行完成再往下走
# # g2.join()
# gevent.sleep(1)
for i in range(10):
    print(i)
