from selenium import webdriver
from time import  sleep
import unittest
import xinyue
from selenium.common.exceptions import NoAlertPresentException

class study(unittest.TestCase):

    def setUp(self):
        print('开始执行')

    def test_logon1(self):
        driver = webdriver.Chrome()
        username = 'admin'
        password = 'admin123'
        xinyue.test_user_login(driver, username, password)
        if alert(driver)==1:
            test = driver.switch_to_alert().text
            driver.switch_to_alert().dismiss()
            self.assertEqual(test,'用户名或密码不正确')
        else:
            title = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/a/small').text
            self.assertEqual(title, '汇佳健康管理中心')


    def test_logon2(self):
        driver = webdriver.Chrome()
        username = 'admin'
        password = 'admin'
        xinyue.test_user_login(driver, username, password)
        if alert(driver)==1:
            test = driver.switch_to_alert().text
            driver.switch_to_alert().dismiss()
            self.assertEqual(test,'用户名或密码不正确')
        else:
            title = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/a/small').text
            self.assertEqual(title, '汇佳健康管理中心')

    def tearDown(self):
        print('执行结束')




def alert(driver):
    try:
        alert = driver.switch_to.alert
        alert.text
        return 1
    except NoAlertPresentException:
        return 2

