from time import sleep
import unittest
from xinyuedata.test_case.models import myunit,function,parameter
from xinyuedata.test_case.page_obj import loginPage
from xinyuedata.test_case.page_obj.entityPage import entity
from xinyuedata.test_case.page_obj.loginPage  import login
from itertools import islice
class Diseases(myunit.MyTest):
    '''
    病种管理
    '''
    #登陆测试
    def user_login_verify(self,username='admin',password='admin123'):
        login(self.driver).user_login(username,password)

    #添加病种，勾选app首页展示
    def diseases_verify(self,diseases):
        self.user_login_verify()#登陆
        po = entity(self.driver)
        po.labelling_button()
        self.driver.switch_to_frame('cframe')
        po.add_button()
        po.entity_input(diseases)
        po.show_click()
        po.save_button()

    #添加病种，勾选app首页展示
    def diseases_verify1(self,diseases):
        self.user_login_verify()#登陆
        po = entity(self.driver)
        po.labelling_button()
        self.driver.switch_to_frame('cframe')
        po.add_button()
        po.entity_input(diseases)
        po.save_button()

    #修改病种
    def modification_ververify(self,diseases):
        po = entity(self.driver)
        po.modification_button()
        po.entity_input_modifi()
        po.entity_input(diseases)
        po.modify_confirm_button()


    #新增病种，勾选首页展示
    def test_add1(self):
        self.diseases_verify('病种1')
        po = entity(self.driver)
        sleep(3)
        assert  self.assertEqual(po.title_alert(self.driver),'操作成功！')
        function.inster_img(self.driver,'new_diseases.jpg')

    #病种重复
    def test_add2(self):
        self.diseases_verify('病种1')
        po = entity(self.driver)
        sleep(3)
        self.assertNotEqual(po.title_alert(self.driver),'病种重复不能重复')
        function.inster_img(self.driver,'repetition_diseases.jpg')

    #病种为空
    def test_add3(self):
        self.diseases_verify('')
        po = entity(self.driver)
        sleep(3)
        self.assertEqual(po.title_alert(self.driver),'病种不能为空')
        function.inster_img(self.driver,'null_diseases.jpg')

    #长度限制
    def test_add4(self):
        self.diseases_verify('一二三四五六七八九十')
        po = entity(self.driver)
        sleep(3)
        self.assertEqual(po.title_alert(self.driver),'操作成功！')
        function.inster_img(self.driver,'Length_diseases.jpg')

    #字符限制
    def test_add5(self):
        self.diseases_verify('123自行车zxc$%&')
        po = entity(self.driver)
        sleep(3)
        assert  self.assertEqual(po.title_alert(self.driver),'操作成功！')
        function.inster_img(self.driver,'character_diseases.jpg')

    #新增病种，不勾选首页展示
    def test_add6(self):
        self.diseases_verify1('病种2')
        po = entity(self.driver)
        sleep(3)
        assert  self.assertEqual(po.title_alert(self.driver),'操作成功！')
        function.inster_img(self.driver,'new1_diseases.jpg')

    #启用病种
    def test_add7(self):
        self.user_login_verify()
        po = entity(self.driver)
        po.labelling_button()
        self.driver.switch_to_frame('cframe')
        po.stop_button()
        self.assertEqual(po.title_alert(self.driver),'操作成功')

    #修改病种
    def test_add8(self):
       po = entity(self.driver)
       self.user_login_verify()#登陆
       #点击病种管理菜单
       po.labelling_button()
       #切换页面
       self.driver.switch_to_frame('cframe')
       #获取当前病种
       h = po.acquiring_button()
       self.modification_ververify(h)
       sleep(1)
       self.assertEqual(po.title_alert(self.driver),'操作成功！')

if __name__ == '__main__':
    unittest.main()





