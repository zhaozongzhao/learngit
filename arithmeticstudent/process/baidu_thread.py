from selenium import webdriver
from threading import Thread
from time import sleep,ctime


def test_baidu(browser,search):
    print(browser,search)
    if browser == 'Chrome':
        driver = webdriver.Chrome()
    elif browser == 'ie':
        driver = webdriver.Ie()
    else:
        print('当前不支持')

    driver.get('http://www.baidu.com')

if __name__ == '__main__':
    #启动参数
    lists = {'Chrome':'测试1','ie':'测试2'}
    #创建线程组
    threads = []
    #获取线程的迭代次数
    files = range(len(lists))
    #创建线程
    for browser,search in lists.items():
         t = Thread(target=test_baidu,args=(browser,search))
         threads.append(t)

    #启动线程
    for t in files:
        threads[t].start()
    for t in  files:
        threads[t].join()
    print('结束： %s'%ctime())