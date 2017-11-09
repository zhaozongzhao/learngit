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

class Title1(unittest.TestCase):

     def setUp(self):
        driver.refresh()
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[1]/ul/li[1]/a/span').click()
        driver.switch_to_frame('cframe')

     def test_add1(self):
         '''职称添加验证'''
         list=read(1)
         Title(driver,list[1])
         time.sleep(0.5)
         h=driver.switch_to_alert().text
         driver.switch_to_alert().dismiss()
         self.assertEqual(h,'操作成功！')

     def test_add2(self):
         '''职称添加验证'''

         Title(driver,'主任医生6')
         time.sleep(0.5)
         h=driver.switch_to_alert().text
         driver.switch_to_alert().dismiss()
         self.assertEqual(h,'操作成功！')

     def tearDown(self):
         driver.refresh()



def  Title(driver,title):

    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div/div/a').click()
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/form/div/div/input').send_keys(title)
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()



def read(h):
    date = csv.reader(open('C:\\csv1\\2.csv','r'))

    for i ,user in enumerate(date):
        #
        if i==h:
            row=user
            return row