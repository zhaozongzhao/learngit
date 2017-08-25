import unittest
from selenium import  webdriver
from selenium.common.exceptions import NoAlertPresentException
import time
from selenium.webdriver.common.action_chains import ActionChains


driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://hj.dryork.cn/huijia/admin/main')
driver.find_element_by_xpath('//*[@id="userid"]').send_keys('admin')
driver.find_element_by_xpath('//*[@id="userpassid"]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="checkNumber"]').send_keys('1234')
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[3]/div[1]/div/div/form/fieldset/div[3]/button').click()

class MyTest2(unittest.TestCase):

  def setUp(self):
     driver.refresh()

  def test_add1(self):
      driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[2]/a/span').click()
      driver.switch_to.frame('cframe')
      driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[4]/div[2]/ul/li[3]/a').click()
      right_click = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[4]/a[2]')
      ActionChains(driver).double_click(right_click).perform()
      time.sleep(0.5)
      test=driver.switch_to_alert().text
      driver.switch_to_alert().dismiss()
      self.assertIn(test,'删除成功')


  def test_add2(self):
      driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[2]/a/span').click()
      driver.switch_to.frame('cframe')
      driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[4]/div[2]/ul/li[3]/a').click()
      right_click = driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[4]/a[2]')
      ActionChains(driver).double_click(right_click).perform()
      time.sleep(0.5)
      test=driver.switch_to_alert().text
      driver.switch_to_alert().dismiss()
      self.assertIn(test,'删除成功')



  def tearDown(self):
       driver.refresh()

if __name__ == '__main__':
       unittest.mian()
