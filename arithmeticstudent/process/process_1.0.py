
from time import sleep,ctime
import multiprocessing


def super_play(files_,time):
    for i in range(2):
        print('播放的音乐是： %s! %s'%(files_,ctime()))
        print('')
        sleep(time)

lists ={'爱情买卖':3,'天使的翅膀':4,'我和你':5}

#创建进程组
process = []

filtes = range(len(lists))

#创建进程
for files_,time in lists.items():
     t = multiprocessing.Process(target=super_play,args=(files_,time))
     process.append(t)

if __name__ == '__main__':
    #启动进程
    for t in filtes:
        process[t].start()
    for t in filtes:
        process[t].join()
    print('结束 ：%s'%ctime())