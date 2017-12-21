from time import sleep
import unittest
from xinyuedata.test_case.models import myunit,function,parameter
from xinyuedata.test_case.page_obj import loginPage
from xinyuedata.test_case.page_obj.upgrade_administerPage  import upgrade
from xinyuedata.test_case.page_obj.loginPage  import login
from itertools import islice



class Reader():
    #读取相关格式的类
    def __init__(self):
        self.systems = 0
        self.edition1 = 0
        self.edition2 = 0
        self.edition3 = 0
        self.headings = 0
        self.prompting = 0
        self.url = 0

    def reader_systems(self):
        #读取系统
        self.systems = []
        list = parameter.read_csv('upgrade.csv')
        for data in islice(list,1,None):
            self.systems.append(data[0])
        return  self.systems

    def reader_edition1(self):
        #读取版本1
        self.edition1 =[]
        list = parameter.read_csv('upgrade.csv')
        for data in islice(list,1,None):
            self.edition1.append(data[1])
        return  self.edition1

    def reader_edition2(self):
        #读取版本2
        self.edition2 =[]
        list = parameter.read_csv('upgrade.csv')
        for data in islice(list,1,None):
            self.edition2.append(data[2])
        return  self.edition2

    def reader_edition3(self):
        #读取版本3
        self.edition3 =[]
        list = parameter.read_csv('upgrade.csv')
        for data in islice(list,1,None):
            self.edition3.append(data[3])
        return  self.edition3

    def reader_headings(self):
        #读取标题
       self.headings=[]
       list = parameter.read_csv('upgrade.csv')
       for data in islice(list,1,None):
            self.headings.append(data[4])
       return  self.headings

    def reader_prompting(self):
        #读取提示
       self.prompting=[]
       list = parameter.read_csv('upgrade.csv')
       for data in islice(list,1,None):
            self.prompting.append(data[5])
       return  self.prompting

    def reader_url(self):
        #读取提示
       self.url=[]
       list = parameter.read_csv('upgrade.csv')
       for data in islice(list,1,None):
            self.url.append(data[5])
       return  self.url

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
    def add_edition_verify(self,system,number1,number2,numbrt3,headings,prompting,url):
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
         if system == 'ios':
            po.ios_system_input()
         elif system == 'android':
            po.android_system_input()
         else:
             print('版本{}'.format(system))
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
        function.inster_img(self.driver,'升级管理_筛选_ios.jpg')

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
        function.inster_img(self.driver,'升级管理_筛选_android.jpg')

    def test_add2(self):
        #功能验证
        r=Reader()
        self.add_edition_verify(
           r.reader_systems()[0],
           r.reader_edition1()[0],
           r.reader_edition2()[0],
           r.reader_edition3()[0],
           r.reader_headings()[0],
           r.reader_prompting()[0],
           r.reader_url()[0]
        )
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'操作成功！')
        function.inster_img(self.driver,'升级管理_添加.jpg')

    def test_add4(self):
        #版本号不能重复
        r=Reader()
        self.add_edition_verify(
           r.reader_systems()[0],
           r.reader_edition1()[0],
           r.reader_edition2()[0],
           r.reader_edition3()[0],
           r.reader_headings()[0],
           r.reader_prompting()[0],
           r.reader_url()[0]
        )
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'平台版本号不能重复')
        function.inster_img(self.driver,'升级管理_添加_版本号重复.jpg')

    def test_add3(self):
        #版本号只能是数字
        r=Reader()
        self.add_edition_verify(
           r.reader_systems()[0],
           r.reader_edition1()[1],
           r.reader_edition2()[1],
           r.reader_edition3()[1],
           r.reader_headings()[1],
           r.reader_prompting()[1],
           r.reader_url()[1]
        )
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'版本号只能是数字')
        function.inster_img(self.driver,'升级管理_添加_版本非数字.jpg')

    def test_add5(self):
        #版本号不能小于当前版本最大号
         r=Reader()
         self.add_edition_verify(
           r.reader_systems()[0],
           r.reader_edition1()[2],
           r.reader_edition2()[2],
           r.reader_edition3()[2],
           r.reader_headings()[2],
           r.reader_prompting()[2],
           r.reader_url()[2]
         )
         sleep(3)
         po = upgrade(self.driver)
         self.assertEqual(po.title_alert(self.driver),'版本号不能小于当前版本')
         function.inster_img(self.driver,'升级管理_添加_版本小于当前.jpg')

    def test_add6(self):
        #版本号不能为空
         r=Reader()
         self.add_edition_verify(
           r.reader_systems()[0],
           r.reader_edition1()[3],
           r.reader_edition2()[3],
           r.reader_edition3()[3],
           r.reader_headings()[3],
           r.reader_prompting()[3],
           r.reader_url()[3]
         )
         sleep(3)
         po = upgrade(self.driver)
         self.assertEqual(po.title_alert(self.driver),'版本号不能为空')
         function.inster_img(self.driver,'升级管理_添加_版本号不能为空.jpg')

    def test_add7(self):
        #版本号不完整
         r=Reader()
         self.add_edition_verify(
           r.reader_systems()[0],
           r.reader_edition1()[4],
           r.reader_edition2()[4],
           r.reader_edition3()[4],
           r.reader_headings()[4],
           r.reader_prompting()[4],
           r.reader_url()[4]
         )
         sleep(3)
         po = upgrade(self.driver)
         self.assertEqual(po.title_alert(self.driver),'请输入完整的版本号')
         function.inster_img(self.driver,'升级管理_添加_版本号不完整.jpg')

    def test_add8(self):
        #版本号不完整
         r=Reader()
         self.add_edition_verify(
           r.reader_systems()[0],
           r.reader_edition1()[5],
           r.reader_edition2()[5],
           r.reader_edition3()[5],
           r.reader_headings()[5],
           r.reader_prompting()[5],
           r.reader_url()[5]
         )
         sleep(3)
         po = upgrade(self.driver)
         self.assertEqual(po.title_alert(self.driver),'请输入完整的版本号')
         function.inster_img(self.driver,'升级管理_添加_版本号不完整.jpg')

    def test_add9(self):
        #版本号不完整
         r=Reader()
         self.add_edition_verify(
           r.reader_systems()[0],
           r.reader_edition1()[6],
           r.reader_edition2()[6],
           r.reader_edition3()[6],
           r.reader_headings()[6],
           r.reader_prompting()[6],
           r.reader_url()[6]
         )
         sleep(3)
         po = upgrade(self.driver)
         self.assertEqual(po.title_alert(self.driver),'请输入完整的版本号')
         function.inster_img(self.driver,'升级管理_添加_版本号不完整.jpg')

    def test_add10(self):
        #测试标题不能为空
         r=Reader()
         self.add_edition_verify(
           r.reader_systems()[0],
           r.reader_edition1()[7],
           r.reader_edition2()[7],
           r.reader_edition3()[7],
           r.reader_headings()[7],
           r.reader_prompting()[7],
           r.reader_url()[7]
         )
         sleep(3)
         po = upgrade(self.driver)
         self.assertEqual(po.title_alert(self.driver),'升级标题不能为空')
         function.inster_img(self.driver,'升级管理_添加_升级标题为空.jpg')

    def test_add11(self):
        #输入格式验证
        r=Reader()
        self.add_edition_verify(
           r.reader_systems()[0],
           r.reader_edition1()[8],
           r.reader_edition2()[8],
           r.reader_edition3()[8],
           r.reader_headings()[8],
           r.reader_prompting()[8],
           r.reader_url()[8]
         )
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'操作成功！')
        function.inster_img(self.driver,'升级管理_添加_格式验证.jpg')

    def test_add11(self):
        #输入长度验证
        r=Reader()
        self.add_edition_verify(
           r.reader_systems()[0],
           r.reader_edition1()[9],
           r.reader_edition2()[9],
           r.reader_edition3()[9],
           r.reader_headings()[9],
           r.reader_prompting()[9],
           r.reader_url()[9]
         )
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'操作成功！')
        function.inster_img(self.driver,'升级管理_添加_长度验证.jpg')

    def test_add12(self):
        #提示信息不能为空
        r=Reader()
        self.add_edition_verify(
           r.reader_systems()[0],
           r.reader_edition1()[10],
           r.reader_edition2()[10],
           r.reader_edition3()[10],
           r.reader_headings()[10],
           r.reader_prompting()[10],
           r.reader_url()[10]
         )
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'升级提示信息不能为空')
        function.inster_img(self.driver,'升级管理_提示信息_为空.jpg')

    def test_add13(self):
        #提示信息输入格式验证
        r=Reader()
        self.add_edition_verify(
           r.reader_systems()[0],
           r.reader_edition1()[11],
           r.reader_edition2()[11],
           r.reader_edition3()[11],
           r.reader_headings()[11],
           r.reader_prompting()[11],
           r.reader_url()[11]
         )
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'操作成功！')
        function.inster_img(self.driver,'升级管理_提示信息_格式验证.jpg')

    def test_add14(self):
        #提示信息输入长度验证
        r=Reader()
        self.add_edition_verify(
           r.reader_systems()[0],
           r.reader_edition1()[12],
           r.reader_edition2()[12],
           r.reader_edition3()[12],
           r.reader_headings()[12],
           r.reader_prompting()[12],
           r.reader_url()[12]
         )
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'操作成功！')
        function.inster_img(self.driver,'升级管理_提示信息_长度验证.jpg')

    def test_add15(self):
        #ios url可以为空
        r=Reader()
        self.add_edition_verify(
            r.reader_systems()[0],
           r.reader_edition1()[13],
           r.reader_edition2()[13],
           r.reader_edition3()[13],
           r.reader_headings()[13],
           r.reader_prompting()[13],
           r.reader_url()[13]
         )
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'操作成功！')
        function.inster_img(self.driver,'升级管理_url_为空.jpg')

    def test_add16(self):
        #ios url格式验证
        r=Reader()
        self.add_edition_verify(
           r.reader_systems()[0],
           r.reader_edition1()[14],
           r.reader_edition2()[14],
           r.reader_edition3()[14],
           r.reader_headings()[14],
           r.reader_prompting()[14],
           r.reader_url()[14]
         )
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'操作失败')
        function.inster_img(self.driver,'升级管理_url_格式验证.jpg')

    def test_add17(self):
        #点击按钮,点击后状态版本发生改变
        self.frame_verify()
        po = upgrade(self.driver)
        list = self.get_list_data_verify()
        po.list_stop_button()
        po.title_alert(self.driver)
        list1 = self.get_list_data_verify()
        self.assertNotEqual(list[6],list1[6])
        function.inster_img(self.driver,'升级管理_修改状态.jpg')


    def test_add18(self):
        #修改功能测试
        self.frame_verify()
        po = upgrade(self.driver)
        po.list_modification_button()
        sleep(0.5)
        po.save_button1()
        sleep(1)
        self.assertEqual(po.title_alert(self.driver),'操作成功！')
        function.inster_img(self.driver,'升级管理_修改功能验证.jpg')

    def test_add19(self):
        #修改医生是否强制升级
        self.frame_verify()
        po = upgrade(self.driver)
        list = self.get_list_data_verify()
        po.list_modification_button()
        sleep(1)
        po.isupupgrade_input()
        po.save_button1()
        sleep(1)
        po.title_alert(self.driver)
        list1 = self.get_list_data_verify()
        self.assertNotEqual(list[5],list1[5])
        function.inster_img(self.driver,'升级管理_更改强制升级状态.jpg')


    def test_add20(self):
        #添加
       #功能验证
        r=Reader()
        self.add_edition_verify(
           r.reader_systems()[15],
           r.reader_edition1()[15],
           r.reader_edition2()[15],
           r.reader_edition3()[15],
           r.reader_headings()[15],
           r.reader_prompting()[15],
           r.reader_url()[15]
        )
        sleep(3)
        po = upgrade(self.driver)
        self.assertEqual(po.title_alert(self.driver),'操作成功！')
        function.inster_img(self.driver,'升级管理_android添加.jpg')







if __name__ == '__main__':
    unittest.main()