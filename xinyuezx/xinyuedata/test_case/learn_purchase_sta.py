from time import sleep
import unittest
from xinyuedata.test_case.models import myunit,function,parameter
from xinyuedata.test_case.page_obj import loginPage
from xinyuedata.test_case.page_obj.learn_purchase_Page import Purchase
from xinyuedata.test_case.page_obj.labellingPage import lebelingPage
from xinyuedata.test_case.page_obj.loginPage  import login
from itertools import islice
from xinyuedata.test_case.models.driver import browser

class operation(Purchase):

    def __init__(self,driver):
        self.driver = driver


     #登录操作
    def user_login_verify(self,username='admin',password='admin123'):
        login(self.driver).user_login(username,password)

    #进入标签页
    def iframe_verify(self):
         lebel = lebelingPage(self.driver)
         self.user_login_verify()
         lebel.learen_guide()

    def list_data(self):
        self.iframe_verify()
        po = Purchase(self.driver)
        lsit = po.data_list()
        return  lsit


class Purchaseadmin(myunit.MyTest):
    '''指南申购管理'''

    def test_list_data_name(self):
        op = operation(self.driver)
        list = op.list_data()
        self.assertEqual(list[1],'病种1')