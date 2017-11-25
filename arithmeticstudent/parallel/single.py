'''
学习多线程
1.单线程

'''
from time import sleep,ctime

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

def main():
    '''
    主函数
    '''
    music('音乐',2)
    movie('阿凡提',2)
    print('all end',ctime())

if __name__ == '__main__':
    main()