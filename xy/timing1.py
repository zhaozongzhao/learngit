# #Python下实现定时任务的方式有很多种方式。
# 循环sleep：
#
# 这是一种最简单的方式，在循环里放入要执行的任务，然后sleep一段时间再执行。缺点是，不容易控制，而且sleep是个阻塞函数
import time
def timer():
    '''''
    每n秒执行一次
    '''
    while True:
        print(time.strftime('%Y-%m-%d %X',time.localtime()))
        # 此处为要执行的任务
        time.sleep(100)

timer()