import unittest#患者管理详细修改
from selenium import  webdriver
from selenium.common.exceptions import NoAlertPresentException
import time
from HTMLTestRunner import  HTMLTestRunner


driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://hj.dryork.cn/huijia/admin/main')
driver.find_element_by_xpath('//*[@id="userid"]').send_keys('admin')
driver.find_element_by_xpath('//*[@id="userpassid"]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="checkNumber"]').send_keys('1234')
driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[3]/div[1]/div/div/form/fieldset/div[3]/button').click()

class details(unittest.TestCase):#详情标签修改

    def setUp(self):
        driver.refresh()
        driver.switch_to_frame('cframe')

    def test_detailsadd1(self):
        test=minute(driver,'由国娟')
        self.assertIsNot(test[0],test[1])

    def test_detailsadd2(self):
        test=minute(driver,'李秉翰')
        self.assertIsNot(test[0],test[1])


    def test_detailsadd2(self):
        test=minute(driver,'刘羽骞')
        self.assertIsNot(test[0],test[1])


    def tearDown(self):
        driver.refresh()


class Remark(unittest.TestCase):#备注信息修改

    def setUp(self):
        driver.refresh()
        driver.switch_to_frame('cframe')

    def test_Remarkadd1(self):
        test = remark(driver,'由国娟',1)
        self.assertNotIn(test[0],test[1])


    def test_Remarkadd3(self):
        test = remark(driver,'由国娟',0)
        self.assertNotIn(test[0],test[1])


    def test_Remarkadd2(self):
        test = remark(driver,'*临时患者',0)
        self.assertNotIn(test[0],test[1])



    def tearDown(self):
         driver.refresh()




def minute(driver,name):#
    driver.find_element_by_xpath('//*[@id="name"]').send_keys(name)
    driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div/div[9]/button').click()
    time.sleep(5)
    test1=driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[3]').text
    print('第一次')
    print(test1)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[10]/a').click()
   #截图查看应版本问题截图暂不好用
    #n='C:\\csv1'+'患者详情'+'.jgp'
    #driver.get_screenshot_as_file(n)
    time.sleep(2)
    inputs = driver.find_elements_by_class_name('modcheckboxs')
    for i in inputs:
        if i.get_attribute('type')=='checkbox':
            i.click()
            time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[1]/div/div/div[2]/div[13]/div[2]/div').click()
    time.sleep(0.5)
    test2=driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[3]').text

    print(test2)
    return  test1,test2


def remark(driver,name,empty):#备注信息修改
    driver.find_element_by_xpath('//*[@id="name"]').send_keys(name)
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div/div[9]/button').click()
    time.sleep(5)
    test1=driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[9]').text
    print('第一次')
    print(test1)
    time.sleep(0.5)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[10]/a').click()
    if empty==1:
       time.sleep(0.5)
       driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[1]/div/div/div[2]/div[12]/div/textarea').clear()
       driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[1]/div/div/div[2]/div[12]/div/textarea').send_keys('备注信息1')
       time.sleep(0.5)
       driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[1]/div/div/div[2]/div[13]/div[2]/div/button').click()
       time.sleep(0.5)
       test2=driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[9]').text
       print('第二次')
    else:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[1]/div/div/div[2]/div[12]/div/textarea').send_keys('11111')
        time.sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[1]/div/div/div[2]/div[13]/div[2]/div/button').click()
        time.sleep(0.5)
        test2=driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[9]').text
        print('第二次')
    print(test2)
    return  test1,test2

if __name__ == '__main__':
      testsuite=unittest.TestSuite
      testsuite.addTest(details('test_Remarkadd1'))
      testsuite.addTest( details('test_Remarkadd2'))
     # runner = unittest.TextTestRunner()
      fp=open('./result.html','wb')
      runner=HTMLTestRunner(stream=fp,title='标签修改测试报告',description='用例测试情况')
      #unittest.mian()
      runner.run(testsuite)
      fp.close()
