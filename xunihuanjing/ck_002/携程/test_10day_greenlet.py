'''
1,展示greenelent ,不能自动切换需要手动切换
'''
import greenlet

def work1():
    for i in range(10):
          print('work1----{}'.format(i))
          g2.switch()    #切换到g2



def work2():
    for i in range(10):
          print('work2----{}'.format(i))
          g1.switch()  #切换到g1



g1 = greenlet.greenlet(work1)  #返回协程对象
g2 = greenlet.greenlet(work2)

g1.switch()  #启动开关
