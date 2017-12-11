from time import sleep
import unittest
from xinyuedata.test_case.models import myunit,function,parameter
from xinyuedata.test_case.page_obj import loginPage
from xinyuedata.test_case.page_obj.foundation_diseasesPage import diseases
from xinyuedata.test_case.page_obj.loginPage  import login
from itertools import islice
class titleTest(myunit.MyTest):
    '''添加职称，点击停用、启用按钮'''

    def user_login_verify(self,username='admin',password='admin123'):
        login(self.driver).user_login(username,password)


    def titleadd_verify(self,title=''):
        #添加职称
        self.driver.switch_to_frame('cframe')
        diseases(self.driver).add_buutton()
        diseases(self.driver).job_title_input(title)
        diseases(self.driver).save_button()

    def operation_verify(self):
        #点击操作
        self.user_login_verify()
        self.driver.switch_to_frame('cframe')
        po = diseases(self.driver)
        po.stop_button()
        h = po.title_alert(self.driver)
        return h

    def state_verify(self):
        #状态判断
        self.user_login_verify()
        self.driver.switch_to_frame('cframe')
        po = diseases(self.driver)
        list = []
        sleep(5)
        list.append(po.type_state())
        sleep(5)
        po.stop_button()
        po.title_alert(self.driver)
        sleep(5)
        list.append(po.type_state())
        return  list


    def test_Add(self):
        #职称重复
        self.user_login_verify()
        po = diseases(self.driver)
        title = parameter.read_csv('title.csv')
        self.titleadd_verify(title='主任医生')
        sleep(2)
        self.assertEqual(po.title_alert(self.driver),'职称不能重复')
        function.inster_img(self.driver,'title_repetition.jpg')

    def test_Add1(self):
        #职称不能为空
        self.user_login_verify()
        po =diseases(self.driver)
        self.titleadd_verify(title='')
        sleep(2)
        self.assertEqual(po.title_alert(self.driver),'职称不能为空')

    def test_Add2(self):
        #职称添加成功
        self.user_login_verify()
        self.titleadd_verify(title='验证测试职位2')
        po = diseases(self.driver)
        sleep(5)
        self.assertEqual(po.title_alert(self.driver),'操作成功！')

    def test_type3(self):
        #点击启用/停用操作按钮
        h = self.operation_verify()
        self.assertEqual(h,'操作成功')

    def test_type4(self):
        #职称状态改变
        list = self.state_verify()
        self.assertNotEqual(list[0],list[1])

    def test_type5(self):
       #获取列表总数
       self.user_login_verify()
       po = diseases(self.driver)
       self.driver.switch_to_frame('cframe')
       txt_str = po.list_quantity()
       self.assertEqual(txt_str,'显示第 1 到第 8 条记录，总共 8 条记录')




if __name__ == '__main__':
    titleTest.operation_verify()