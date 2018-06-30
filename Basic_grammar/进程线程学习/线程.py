import time,threading

#新线程执行的代码
def loop():
    print('thread {} 开始执行'.format(threading.current_thread().name))
    n = 0
    while n < 5:
        n = n + 1
        print('thread {} 第{}次'.format(threading.current_thread().name,n))
        time.sleep(1)
    print('thread {} 执行结束'.format(threading.current_thread().name))

print('线程{}开始'.format(threading.current_thread().name))
t = threading.Thread(target=loop,name='循环')
t.start()
t.join()
print('线程{}执行结束'.format(threading.current_thread().name))
