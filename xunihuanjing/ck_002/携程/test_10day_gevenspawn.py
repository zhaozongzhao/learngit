'''
1,协程gevent IO操作会切换
2.写好协程传参
'''
import gevent,requests



import time
def func2(func):
    print('运行装饰器')

    def wrapper():
        stime = time.time()  # 获取开始运行时间
        func()
        etime = time.time()  # 获取结束时间
        print('程序运行时间{}秒'.format(etime - stime))

    return wrapper


def work1(url,i=None):  # 工作任务
    print(i)
    headers = {

        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    for i in range(10):
        requests.get(url,headers=headers)
        print('第{}次请求'.format(i))
        gevent.sleep(0.001)

@func2
def main():

    g1 = gevent.spawn(work1,url = 'https://www.baidu.com') #指定工作函数
    g2 = gevent.spawn(work1,'http://smart.sqbj.com/login','111') #指定工作函数
    g1.join()    #主协程等待子协程执行完成再往下走
    g2.join()


if __name__ == '__main__':
    main()