from selenium import  webdriver#测试登陆
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import csv
from HTMLTestRunner import HTMLTestRunner
class MyTest(unittest.TestCase):
  '''检大夫登录测试'''
  def setUp(self):
     self.driver=webdriver.Chrome()
     #self.driver.maximize_window()
     self.driver.implicitly_wait(10)
     self.base_url = 'http://101.201.78.244:8098/jiandaifu_manage/admin/main'

  def test_login1(self):
     '''登楼界面验证'''
     driver = self.driver
     driver.get(self.base_url)
     list=read(1)
     login(driver,list[1],list[2])
     time.sleep(5)
     x=alert(driver)
     if x==1:
         test=driver.switch_to_alert().text
         driver.switch_to_alert().dismiss()
         self.assertEqual(test,'用户名或密码不正确')
     else:
        title=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/a/small').text
        self.assertEqual(title,'检大夫后台管理系统')



  def test_login2(self):
     '''登楼界面验证'''
     driver = self.driver
     driver.get(self.base_url)
     list=read(2)
     login(driver,list[1],list[2])
     time.sleep(5)
     x=alert(driver)
     if x==1:
         test=driver.switch_to_alert().text
         driver.switch_to_alert().dismiss()
         self.assertEqual(test,'用户名或密码不正确')
     else:
        title=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/a/small').text
        self.assertEqual(title,'检大夫后台管理系统')





  def test_login3(self):
     '''登楼界面验证'''
     driver = self.driver
     driver.get(self.base_url)
     time.sleep(5)
     list=read(3)
     login(driver,list[1],list[2])
     time.sleep(5)
     x=alert(driver)
     if x==1:
         test=driver.switch_to_alert().text
         driver.switch_to_alert().dismiss()
         self.assertEqual(test,'用户名或密码不正确')
     else:
        title=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/a/small').text
        self.assertEqual(title,'检大夫后台管理系统')




  def test_login4(self):
     '''登楼界面验证'''
     driver = self.driver
     driver.get(self.base_url)
     list=read(4)
     login(driver,list[1],list[2])
     time.sleep(5)
     x=alert(driver)
     if x==1:
         test=driver.switch_to_alert().text
         driver.switch_to_alert().dismiss()
         self.assertEqual(test,'用户名或密码不正确')
     else:
        title=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/a/small').text
        self.assertEqual(title,'检大夫后台管理系统')




  def test_login5(self):
     '''登楼界面验证'''
     driver = self.driver
     driver.get(self.base_url)
     list=read(5)
     login(driver,list[1],list[2])
     time.sleep(5)
     x=alert(driver)
     if x==1:
         test=driver.switch_to_alert().text
         driver.switch_to_alert().dismiss()
         self.assertEqual(test,'用户名或密码不正确')
     else:
        title=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/a/small').text
        self.assertEqual(title,'检大夫后台管理系统')




  def test_login6(self):
     '''登楼界面验证'''
     driver = self.driver
     driver.get(self.base_url)
     login(driver,list[1],list[2])
     time.sleep(5)
     x=alert(driver)
     if x==1:
         test=driver.switch_to_alert().text
         driver.switch_to_alert().dismiss()
         self.assertEqual(test,'用户名或密码不正确')
     else:
        title=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/a/small').text
        self.assertEqual(title,'检大夫后台管理系统')




  def tearDown(self):
      self.driver.quit()


if __name__ == '__mian__':
    test=unittest.TestSuite()
    test.addTest(MyTest('test_login1'))
    now=time.strftime('%Y-%m-%d %H-%m-%M')
    #定位用例存放位置
    fp=open("./result"+now+".html",'wb')
    runner=HTMLTestRunner(stream=fp,title='测试报告',description=u'用例执行情况:')
    runner.run(test)
    fp.close()


def login(driver,username,password):
     driver.find_element_by_xpath('//*[@id="userid"]').send_keys(username)
     driver.find_element_by_xpath('//*[@id="userpassid"]').send_keys(password)
     driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[3]/div[1]/div/div/form/fieldset/div[2]/button').click()


def read(h):
    date = csv.reader(open('C:\\csv1\\2.csv','r'))

    for i ,user in enumerate(date):
        #
        if i==h:
            row=user
            return row

def alert(driver):
    #判断

     try:
            alert = driver.switch_to.alert
            alert.text
            return 1
     except NoAlertPresentException:
            return 2