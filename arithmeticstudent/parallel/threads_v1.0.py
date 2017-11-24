'''
学习多线程
1.多线程
2.thread库没有守护线程，threading 模块支持守护线程
备注：没创建一个线程特别麻烦
'''
from time import sleep,ctime
import threading


def music(func,loop):
    '''
    听音乐
    '''
    for i in range(loop):
      print('I was listning to music! %s! %s '%(func,ctime()))
      sleep(2)

def movie(func,loop):

        for i in range(loop):
          print('I was at the movies!%s! %s '%(func,ctime()))
          sleep(5)

def plot(func,loop):

     for i in  range(loop):
          print('I was at the movies!%s! %s '%(func,ctime()))
          sleep(5)





def main():
    '''
    主函数
    '''
    #创建线程组
    threads = []

    #创建线程t1，并添加到线程数组
    t1= threading.Thread(target=music,args=('音乐',2))
    threads.append(t1)

    #创建线程T2,并添加到线程数组

    t2 = threading.Thread(target=movie,args=('阿凡提',2))
    threads.append(t2)

    #启动进程
    for t in  threads:
        t.start()
    #守护线程
    for t in threads:
        t.join()
    print('all end: %s'%ctime())


if __name__ == '__main__':

     main()