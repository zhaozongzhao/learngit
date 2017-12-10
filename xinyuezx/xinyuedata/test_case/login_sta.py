from time import sleep
import unittest
from xinyuedata.test_case.models import myunit,function,parameter
from xinyuedata.test_case.page_obj import loginPage
from xinyuedata.test_case.page_obj.loginPage  import login

class loginTest(myunit.MyTest):
    '''约克登陆测试'''
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
        function.inster_img(self.driver,'user_password_empty.jpg')

    def test_login1(self):
        '''
        用户名正确，密码为空
        '''
        self.user_login_verify(username='admin')
        po = login(self.driver)
        self.assertEqual(po.user_error_hini(self.driver),'密码不能为空')
        function.inster_img(self.driver,'password_empty.jpg')

    def test_login3(self):
        '''
        用户名为空，密码错误
        '''
        self.user_login_verify(password='admin123')
        po = login(self.driver)
        self.assertEqual(po.user_error_hini(self.driver),'用户名不能为空')
        function.inster_img(self.driver,'user_password_empty.jpg')

    def  test_login4(self):
        '''
        用户名，密码错误
        '''
        self.user_login_verify(username='admi',password='123')
        po = login(self.driver)
        self.assertEqual(po.user_error_hini(self.driver),'用户名或密码不正确')
        function.inster_img(self.driver,'user_pass_werror.jpg')

    def test_login5(self):
        '''
        用户名错误
        '''
        self.user_login_verify(username='ssss',password='admin123')
        po = login(self.driver)
        self.assertEqual(po.user_error_hini(self.driver),'用户名或密码不正确')
        function.inster_img(self.driver,'user_error.jpg')

    def test_login6(self):
        '''
        密码错误
        '''
        self.user_login_verify(username='admin',password='123456')
        po = login(self.driver)
        self.assertEqual(po.user_error_hini(self.driver),'用户名或密码不正确')
        function.inster_img(self.driver,'psss_error.jpg')


    def test_login7(self):
         '''
         用户名，密码正确
         '''
         self.user_login_verify('admin',password='admin123')
         po = login(self.driver)
         self.assertEqual(po.user_login_success(),'心悦后台管理系统')
         function.inster_img(self.driver,'user_login_syccess.jpg')



if __name__ == '__main__':
    unittest.main()

