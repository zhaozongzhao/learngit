'''
学习多线程
1.多线程
2.thread库没有守护线程，threading 模块支持守护线程

版本2.0没创建一个线程特别麻烦，进行线程优化
'''


from time import sleep,ctime
import threading


def super_player(file_,time):
    '''创建播放器'''
    for i in range(2):
        print('Start playing : %s！ %s'%(file_,ctime()))
        sleep(time)
#节目字典
list = {'爱情买卖':6,'阿凡达':5,'一条狗的人人生':4}

files = range(len(list))
print(files)

#创建线程数组
threds = []

#创建线程
for file_,time in list.items():
    print(files,time)
    t = threading.Thread(target=super_player,args=(file_,time))
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