from selenium import webdriver
import time
import unittest
import csv
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://101.201.78.244:8098/jiandaifu_manage/admin/main')
driver.find_element_by_xpath('//*[@id="userid"]').send_keys('admin')
driver.find_element_by_xpath('//*[@id="userpassid"]').send_keys('admin123')
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[3]/div[1]/div/div/form/fieldset/div[2]/button').click()

class Page(object):
    '''基础类，用于页面继承'''

    login_url = 'http://101.201.78.244:8098/jiandaifu_manage/admin/main'

    def __init__(self,driver,base_url=login_url):
        '''定义驱动 driver ,基本的url\
         ,超时时间'''
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30


    def on_page(self):
        return self.driver.current_url == (self.base_url+self.url)

    def _open(self,url):
        url=self.base_url+url
        self.driver.get(url)
        assert self.on_page(),'did not land on %s'%url

    def open(self):
        self._open(self.url)


    def find_element(self,*loc):
        return self.driver.find_element(*loc)