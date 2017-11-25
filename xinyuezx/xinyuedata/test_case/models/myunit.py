'''
定义 Mytest()类用于继承unittest.TestCase 类 ，因为执行的测试用例相同，所以抽象为mytest
'''

from selenium import webdriver
from .driver import browser
import unittest
import os


class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver =  browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()