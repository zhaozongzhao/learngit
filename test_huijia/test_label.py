import unittest                             #标签管理添加
from selenium import  webdriver
from selenium.common.exceptions import NoAlertPresentException
import time#
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://hj.dryork.cn/huijia/admin/main')
driver.find_element_by_xpath('//*[@id="userid"]').send_keys('admin')
driver.find_element_by_xpath('//*[@id="userpassid"]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="checkNumber"]').send_keys('1234')
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[3]/div[1]/div/div/form/fieldset/div[3]/button').click()

class MyTest2(unittest.TestCase):
  '''检大夫登陆测试用例'''

  def setUp(self):
    driver.refresh()

  def test_add2(self):#添加标签
      driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[2]/a/span').click()
      driver.switch_to.frame('cframe')
      driver.find_element_by_xpath('//*[@id="showSave-btn"]').click()
      driver.find_element_by_xpath('//*[@id="labelName"]').send_keys('添加1')
      driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[1]/div/div/div[2]/div[3]/div[2]/div/button').click()
      time.sleep(0.5)
      test=driver.switch_to_alert().text
      driver.switch_to_alert().dismiss()
      self.assertIn(test,'添加成功')
      print(test)

  def test_add3(self):#添加标签
       driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[2]/a/span').click()
       driver.switch_to.frame('cframe')
       driver.find_element_by_xpath('//*[@id="showSave-btn"]').click()
       driver.find_element_by_xpath('//*[@id="labelName"]').send_keys('添加8')
       driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[1]/div/div/div[2]/div[3]/div[2]/div/button').click()
       time.sleep(0.5)
       time.sleep(0.5)
       test=driver.switch_to_alert().text
       driver.switch_to_alert().dismiss()
       self.assertIn(test,'添加成功')



  def test_add1(self):#添加标签
       driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[2]/a/span').click()
       driver.switch_to.frame('cframe')
       driver.find_element_by_xpath('//*[@id="showSave-btn"]').click()
       driver.find_element_by_xpath('//*[@id="labelName"]').send_keys('1111111111111111111111')
       driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[1]/div/div/div[2]/div[3]/div[2]/div/button').click()
       time.sleep(0.5)
       time.sleep(0.5)
       test=driver.switch_to_alert().text
       driver.switch_to_alert().dismiss()
       self.assertIn(test,'添加成功')

  def tearDown(self):
      driver.refresh()






if __name__ =='__mian__':
    unittest.mian()




def check(amount):#截取字段
     substr='共'
     l=amount.rfind(substr)
     h=amount[l+1:-3]
     w=h.strip().lstrip().rstrip(' ')
     sum=int(w)
     return sum

def alert(driver):#d判断是否有alert
     try:
            alert = driver.switch_to.alert
            alert.text
            return 1
     except NoAlertPresentException:
            return 2


