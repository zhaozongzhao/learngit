'''amount='显示第 1 到第 10 条记录，总共 23 条记录'
substr='共'
l=amount.rfind(substr)
print(l)
h=amount[l+1:-3]
print(h)
w=h.strip().lstrip().rstrip(' ')
print(w)'''
import unittest
from selenium import  webdriver
from selenium.common.exceptions import NoAlertPresentException
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://hj.dryork.cn/huijia/admin/main')
driver.find_element_by_xpath('//*[@id="userid"]').send_keys('admin')
driver.find_element_by_xpath('//*[@id="userpassid"]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="checkNumber"]').send_keys('1234')
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[3]/div[1]/div/div/form/fieldset/div[3]/button').click()
driver.switch_to.frame('cframe')

driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div/div[6]/div/div/input').send_keys('2017-08-24')
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div/div[7]/div/div/input').send_keys('2030-12-30')
time.sleep(0.5)
driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div/div[9]/button').click()


'''class Member(driver):

  def setUp(self):
       driver.refresh()

  def add1(self):
    test=member(driver)
    x=check(test)
    self.assertEqual(x,80)


  def add2(self):
    test=member(driver)
    x=check(test)
    self.assertEqual(x,83)

  def tearDown(self):
       driver.refresh()'''
