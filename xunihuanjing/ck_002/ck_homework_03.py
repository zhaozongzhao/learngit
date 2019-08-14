# 1、一个完整的闭包须满足那几个个条件？
"""
1.函数中嵌套一个函数
2.外层函数的返回值是内层函数的函数名
3.内层嵌套函数对外层作用域有一个非全局作用域发的引用

"""
#  2、定义一个计算函数运行时间的装饰器（计算时间`使用time模块实现）

import time
def func2(func):
    print('运行装饰器')

    def wrapper():
        stime = time.time()  # 获取开始运行时间
        func()
        etime = time.time()  # 获取结束时间
        print('程序运行时间{}秒'.format(etime - stime))

    return wrapper

@func2
def func():
    time.sleep(5)
    print('运行结束')


#  3、编写装饰器，为多个函数加上登录认证的功能（设置个默认的初始账号密码），
# 要求登录成功一次，后续的函数都无需再输入用户名和密码
import unittest
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://mail.qq.com/')
# 该方法用来确认元素是否存在，如果存在返回flag = true，否则返回false
def isElementExist(element):
    flag = True
    try:
        driver.find_element_by_xpath(element)
        return flag

    except:
        flag = False
        return flag


def login_status(func):
    accouns = {'name': 'xxxx', 'ps': 'xxxx'}  # 设置默认的账户密码

    def wrapper():
        if isElementExist('/html/body/div/div[1]/a'):  # 判断访问页面，如果是登录
            driver.switch_to.frame('login_frame')
            driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
            time.sleep(0.5)
            driver.find_element_by_xpath('//*[@id="u"]').send_keys(accouns['name'])
            driver.find_element_by_xpath('//*[@id="p"]').send_keys(accouns['ps'])
            driver.find_element_by_xpath('//*[@id="login_button"]').click()
            func()
        else:
            func()

    return wrapper


@login_status
def test_01():
    """
    进入草稿箱
   """
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="folder_4"]').click()


@login_status
def test_02():
    """
    进入已发送邮箱
   """
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="folder_3"]').click()


if __name__ == '__main__':
    # func()
    test_01()
    test_02()
