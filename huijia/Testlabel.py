from login import login
import unittest
from selenium import  webdriver
driver=webdriver.Chrome()

'''class TestLabel(unittest.TestCase):
    def setUp(self,driver):
        driver.refresh()
    def tset_label(self,driver):
        h=label.add(driver,'测试1')
        self.assertEqual(h,19)
    def tset_labe2(self,driver):
        h=label.add(driver,'测试2')
        self.assertEqual(h,20)
    def tset_labe3(self,driver):
        h=label.add(driver,'测试3')
        self.assertEqual(h,21)
    def tearDown(self,driver):
        driver.refresh()'''''

class Testlogin(unittest.TestCase):
    def setUp(self):
        pass
    def Test_login(self):
        h=login.login(driver,'admin','123456','1234')
        self.assertTrue(h)
    def tearDown(self):
        pass
