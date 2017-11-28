from time import sleep
import unittest
from xinyuedata.test_case.models import myunit,function
from xinyuedata.test_case.page_obj import loginPage
from xinyuedata.test_case.page_obj.foundation_diseasesPage import diseases
from xinyuedata.test_case.page_obj.loginPage  import login
class titleAdd(myunit.MyTest):
    '''职称添加测试'''

    def user_login_verify(self,username='admin',password='admin123'):
        login(self.driver).user_login(username,password)


    def titleadd_verify(self,title=''):
        self.driver.switch_to_frame('cframe')
        diseases(self.driver).add_buutton()
        diseases(self.driver).job_title_input(title)
        diseases(self.driver).save_button()



    def test_Add(self):
        self.user_login_verify()
        po = diseases(self.driver)
        self.titleadd_verify(title='111')
        sleep(2)
        self.assertEqual(po.title_alert(self.driver),'职称不能重复')
        function.inster_img(self.driver,'title_repetition.jpg')


if __name__ == '__main__':
    unittest.main()