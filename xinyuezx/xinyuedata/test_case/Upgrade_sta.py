from time import sleep
import unittest
from xinyuedata.test_case.models import myunit,function,parameter
from xinyuedata.test_case.page_obj import loginPage
from xinyuedata.test_case.page_obj.upgrade_administerPage  import upgrade
from xinyuedata.test_case.page_obj.loginPage  import login
from itertools import islice

class upgradeTest(myunit.MyTest):
    '''
    升级管理界面测试
    '''
    #登陆
    def user_login_verify(self,username='admin',password='admin123'):
        login(self.driver).user_login(username,password)

    #切换表单
    def frame_verify(self):

        self.user_login_verify()
        po = upgrade(self.driver)
        po.upgrade_administer_labelling()
        self.driver.switch_to_frame('cframe')

    #获取列表数据
    def get_list_data_verify(self):
        #获取列表数据
        po = upgrade(self.driver)
        list = po.list_data()
        return list


    #添加版本
    def add_edition_verify(self,number1,number2,numbrt3,headings,prompting,url):
         '''
         number1: 版本框1
         number2: 版本框2
         numbrt3: 版本框3
         headings:  标题
         prompting: 提示
         url: 升级地址
        '''
         self.frame_verify()
         po = upgrade(self.driver)
         po.new_button()
         sleep(0.5)
         po.ios_system_input()
         po.Version_number_input(number1,number2,numbrt3)
         po.upgrade_headings_input(headings)
         po.upgrade_prompting_input(prompting)
         po.upgrade_url_input(url)
         po.save_button()


    def test_add(self):
        #筛选条件测试-ios
        self.frame_verify()
        po = upgrade(self.driver)
        po.screening_system_input('ios')
        po.enquires_button()
        sleep(0.5)
        list = self.get_list_data_verify()
        for i in list:
            self.assertNotIn('ANDROID',i,'存在{}包含在列表中！ '.format(i))

    def test_add1(self):
        #筛选条件测试-android
        self.frame_verify()
        po = upgrade(self.driver)
        po.screening_system_input('android')
        po.enquires_button()
        sleep(0.5)
        list = self.get_list_data_verify()
        for i in list:
            self.assertNotIn('IOS',i,'存在{}包含在列表中！ '.format(i))

    def test_add2(self):
        #功能验证
        self.add_edition_verify(2,0,2,'测试验证','这是一个测试版本','https://www.baidu.com/')
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'操作成功！')

    def test_add4(self):
        #版本号不能重复
        self.add_edition_verify(2,0,1,'测试验证','这是一个测试版本','https://www.baidu.com/')
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'平台版本号不能重复')

    def test_add3(self):
        #版本号只能是数字
        self.add_edition_verify('s','%',6,'测试验证','这是一个测试版本','https://www.baidu.com/')
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'版本号只能是数字')

    def test_add5(self):
        #版本号不能小于当前版本最大号
        self.add_edition_verify(1,1,1,'测试验证','这是一个测试版本','https://www.baidu.com/')
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'版本号不能小于当前版本')

    def test_add6(self):
        #版本号不能为空
        self.add_edition_verify('','','','测试验证','这是一个测试版本','https://www.baidu.com/')
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'版本号不能为空')

    def test_add7(self):
        #版本号不完整
        self.add_edition_verify(1,'','','测试验证','这是一个测试版本','https://www.baidu.com/')
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'请输入完整的版本号')

    def test_add8(self):
        #版本号不完整
        self.add_edition_verify(1,1,'','测试验证','这是一个测试版本','https://www.baidu.com/')
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'请输入完整的版本号')

    def test_add9(self):
        #版本号不完整
        self.add_edition_verify('',1,1,'测试验证','这是一个测试版本','https://www.baidu.com/')
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'请输入完整的版本号')

    def test_add10(self):
        #测试标题不能为空
        self.add_edition_verify(1,1,1,'','这是一个测试版本','https://www.baidu.com/')
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'升级标题不能为空')

    def test_add11(self):
        #输入格式验证
        self.add_edition_verify(2,0,3,'Aa#$%%$154564','这是一个测试版本','https://www.baidu.com/')
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'操作成功！')

    def test_add11(self):
        #输入长度验证
        self.add_edition_verify(2,0,4,'一二三四五六七八九十一二三四五六七八九十','这是一个测试版本','https://www.baidu.com/')
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'操作成功！')

    def test_add12(self):
        #提示信息不能为空
        self.add_edition_verify(1,1,1,'1','','https://www.baidu.com/')
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'升级提示信息不能为空')

    def test_add13(self):
        #提示信息输入格式验证
        self.add_edition_verify(2,0,5,'1','#￥%Ad156好子','https://www.baidu.com/')
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'操作成功！')

    def test_add14(self):
        #提示信息输入长度验证
        self.add_edition_verify(2,0,6,'1','一二三四五六七八九十/t一二三四五六七八九十','https://www.baidu.com/')
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'操作成功！')

    def test_add15(self):
        #ios url可以为空
        self.add_edition_verify(2,0,7,'1','一二三四五六七八九十/t一二三四五六七八九十','')
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'操作成功！')

    def test_add16(self):
        #ios url格式验证
        self.add_edition_verify(1,1,1,'1','一二三四五六七八九十/t一二三四五六七八九十','sss')
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'操作失败')

    def test_add17(self):
        #点击按钮,点击后状态版本发生改变
        self.frame_verify()
        po = upgrade(self.driver)
        list = self.get_list_data_verify()
        po.list_stop_button()
        po.title_alert(self.driver)
        list1 = self.get_list_data_verify()
        self.assertNotEqual(list[6],list1[6])


    def test_add18(self):
        #修改功能测试
        self.frame_verify()
        po = upgrade(self.driver)
        po.list_modification_button()
        sleep(0.5)
        po.save_button1()
        sleep(1)
        self.assertEqual(po.title_alert(self.driver),'操作成功！')

    def test_add19(self):
        #修改医生是否强制升级
        self.frame_verify()
        po = upgrade(self.driver)
        list = self.get_list_data_verify()
        po.list_modification_button()
        po.isupupgrade_input()
        po.save_button1()
        sleep(1)
        po.title_alert(self.driver)
        list1 = self.get_list_data_verify()
        self.assertNotEqual(list[6],list1[6])








if __name__ == '__main__':
    unittest.main()