from time import sleep
import unittest
from xinyuedata.test_case.models import myunit,function,parameter
from xinyuedata.test_case.page_obj import loginPage
from xinyuedata.test_case.page_obj.learn_guide_purchase_Page import Purchase
from xinyuedata.test_case.page_obj.labellingPage import lebelingPage
from xinyuedata.test_case.page_obj.loginPage  import login
from itertools import islice
from xinyuedata.test_case.models.driver import browser

class GuidePurchase(myunit.MyTest):
    '''指南申购管理界面'''
    #指南申购管理

    #登录操作
    def user_login_verify(self,username='admin',password='admin123'):
        login(self.driver).user_login(username,password)

    #进入标签页
    def iframe_verify(self):
         lebel = lebelingPage(self.driver)
         self.user_login_verify()
         lebel.learen_guide_purchase()


    def list_data(self):
        self.iframe_verify()
        po = Purchase(self.driver)
        h = po.data_list()
        


    def test_purchase_is_determine(self):
        '''存在申请人，手机号码验证'''

        self.iframe_verify()
        po = Purchase(self.driver)
        h = po.data_list()
        self.assertEqual('18301565568',h,'购买信息存在')

    def test_purchase_is_phone_null(self):
        '''不存在患者的手机号码验证'''
        self.iframe_verify()
        po = Purchase(self.driver)
        h = po.data_list()
        self.assertNotEqual('10000000000',h,'购买信息不存在')

    def test_purchase_is_Null(self):
          self.iframe_verify()
          po = Purchase(self.driver)
          h = po.data_list()
          self.assertNotEqual('Null',h,'元素显示为空')



if __name__ == '__main__':
    unittest.main()

