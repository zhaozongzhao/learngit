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

class Doctor(unittest.TestCase):#医生

  def setUp(self):
    driver.refresh()
    driver.switch_to.frame('cframe')
  def test_Doctoradd1(self):
    test=doctor(driver,'刘羽骞')
    x=check(test)
    self.assertEqual(x,1)

  def test_Doctoradd2(self):
    test=doctor(driver,'王瑶')
    x=check(test)
    self.assertEqual(x,4)

  def tearDown(self):
     driver.refresh()

class Tag(unittest.TestCase):#标签

  def setUp(self):
    driver.refresh()
    driver.switch_to.frame('cframe')

  def test_Tagadd1(self):
    test=tag(driver)
    x=check(test)
    self.assertEqual(x,4)

  def test_Tagadd2(self):
    test=tag(driver)
    x=check(test)
    self.assertEqual(x,3)


  def tearDown(self):
     driver.refresh()


class AAA(unittest.TestCase):#会员日期

  def setUp(self):
       driver.refresh()
       driver.switch_to.frame('cframe')
  def test_AAAadd1(self):
    test=Timescreen(driver)
    x=check(test)
    self.assertEqual(x,80)


  def test_AAAadd2(self):
    test=Timescreen(driver)
    x=check(test)
    self.assertEqual(x,80)



  def tearDown(self):
     driver.refresh()


class Member(unittest.TestCase):#会员状态

   def setUp(self):
       driver.refresh()
       driver.switch_to.frame('cframe')


   def test_Memberadd1(self):
       test =  member(driver)
       x=check(test)
       self.assertEqual(x,80)

   def tearDown(self):
     driver.refresh()


class mixture(unittest.TestCase):#组合筛选

    def setUp(self):
        driver.refresh()
        driver.switch_to.frame('cframe')
    def test_mixtureadd1(self):
      doctor(driver,'刘羽骞')
      tag(driver)
      test=member(driver)
      x=check(test)
      self.assertEqual(x,80)


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

def doctor(driver,name):

    driver.find_element_by_xpath('//*[@id="name"]').send_keys(name)
    driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div/div[9]/button').click()
    time.sleep(0.5)
    test=driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[4]/div[1]/span[1]').text
    return test

def tag(driver):

    tag=driver.find_element_by_xpath('//*[@id="labelId"]')
    tag.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div/div[2]/div/select/option[2]').click()
    driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div/div[9]/button').click()
    time.sleep(0.5)
    test=driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[4]/div[1]/span[1]').text
    return test



def Timescreen(driver):

    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div/div[6]/div/div/input').send_keys('2017-08-24')
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div/div[7]/div/div/input').send_keys('2030-12-30')
    time.sleep(0.5)
    driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div/div[9]/button').click()
    time.sleep(0.5)
    test=driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[4]/div[1]/span[1]').text
    return test

def member(driver):

    membe=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div/div[3]/div/select')
    membe.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/div/div[3]/div/select/option[5]').click()
    driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div/div[9]/button').click()
    time.sleep(0.5)
    test=driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[4]/div[1]/span[1]').text
    return test
