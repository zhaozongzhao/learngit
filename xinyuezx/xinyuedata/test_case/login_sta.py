from time import sleep
import unittest
from xinyuedata.test_case.models import myunit,function
from xinyuedata.test_case.page_obj import loginPage
from xinyuedata.test_case.page_obj.loginPage  import login

class loginTest(myunit.MyTest):
    #测试用户登陆
    def user_login_verify(self,username='',password=''):
        login(self.driver).user_login(username,password)

    def test_login(self):
        '''
        用户名，密码为空的登陆
        '''
        self.user_login_verify()
        po = login(self .driver)
        #function.inster_img(self.driver,'user')
        sleep(1)
        self.assertEqual(po.user_error_hini(self.driver),'用户名不能为空')
        self.assertEqual(po.user_error_hini(self.driver),'密码不能为空')
        function