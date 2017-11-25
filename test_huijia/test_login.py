from selenium import  webdriver#测试登陆
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time

class MyTest(unittest.TestCase):
  def setUp(self):
     self.driver=webdriver.Chrome()
     #self.driver.maximize_window()
     self.driver.implicitly_wait(10)
     self.base_url = 'http://hj.dryork.cn/huijia/admin/main'

  def test_login(self):
     driver = self.driver
     driver.get(self.base_url)
     driver.find_element_by_xpath('//*[@id="userid"]').send_keys('admin1')
     driver.find_element_by_xpath('//*[@id="userpassid"]').send_keys('123456')
     driver.find_element_by_xpath('//*[@id="checkNumber"]').send_keys('1234')
     driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[3]/div[1]/div/div/form/fieldset/div[3]/button').click()
     x=alert(driver)
     if x==1:
         test=driver.switch_to_alert().text
         driver.switch_to_alert().dismiss()
         print(test)
     else:
        title=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/a/small').text
        self.assertEqual(title,'汇佳健康管理中心')

  def test_login1(self):
     driver = self.driver
     driver.get('http://hj.dryork.cn/huijia/admin/main')
     driver.find_element_by_xpath('//*[@id="userid"]').send_keys('admin')
     driver.find_element_by_xpath('//*[@id="userpassid"]').send_keys('admin123')
     driver.find_element_by_xpath('//*[@id="checkNumber"]').send_keys('1234')
     driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[3]/div[1]/div/div/form/fieldset/div[3]/button').click()
     time.sleep(5)
     x=alert(driver)
     if x==1:
         test=driver.switch_to_alert().text
         driver.switch_to_alert().dismiss()
         print(test)
     else:
        title=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/a/small').text
        self.assertEqual(title,'汇佳健康管理中心')

  def test_login2(self):
     driver = self.driver
     driver.get('http://hj.dryork.cn/huijia/admin/main')
     driver.find_element_by_xpath('//*[@id="userid"]').send_keys('admin1')
     driver.find_element_by_xpath('//*[@id="userpassid"]').send_keys('123456')
     driver.find_element_by_xpath('//*[@id="checkNumber"]').send_keys('1234')
     driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[3]/div[1]/div/div/form/fieldset/div[3]/button').click()
     x=alert(driver)
     if x==1:
         test=driver.switch_to_alert().text
         driver.switch_to_alert().dismiss()
         print(test)
     else:
        title=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/a/small').text
        self.assertEqual(title,'汇佳健康管理中心')

  def tearDown(self):
       self.driver.quit()

def mian():
    test_login1()


if __name__ =='__mian__':
    unittest.mian()


def alert(driver):
     try:
            alert = driver.switch_to.alert
            alert.text
            return 1
     except NoAlertPresentException:
            return 2



















