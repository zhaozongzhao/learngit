from threading import Thread,Lock
import time


def func2(func):
    """
    装饰器:计算运行时间
    """
    print('运行装饰器')

    def wrapper():
        stime = time.time()  # 获取开始运行时间
        func()
        etime = time.time()  # 获取结束时间
        print('程序运行时间{}秒'.format(etime - stime))

    return wrapper


def work1(name):
    for i in range(6):
        time.sleep(1)
        print('{}绣毯子{}次'.format(name,i))


def work2():
    for i in range(6):
        time.sleep(1)
        print('浇花{}次'.format(i))

#创建线程锁
meto = Lock()

@func2
def main():
    _T1 = Thread(target=work1,args=('zzz',))  # 指定任务不能待"()"
    _T1.start()
    _T2 = Thread(target=work2)
    _T2.start()
    # 设备主线程等待子线程执行结束后再往下执行
    _T1.join()
    _T2.join()
    print('----主线程执行mian函数执行完毕---')


if __name__ == '__main__':
    main()
    print('---主线程执行结束后的代码-----')

