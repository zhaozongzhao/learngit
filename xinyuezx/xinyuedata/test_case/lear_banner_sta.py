from time import sleep
import unittest
from xinyuedata.test_case.models import myunit,function,parameter
from xinyuedata.test_case.page_obj import loginPage
from xinyuedata.test_case.page_obj.learn_banner_Page import Banner
from xinyuedata.test_case.page_obj.labellingPage import lebelingPage
from xinyuedata.test_case.page_obj.loginPage  import login
from itertools import islice
from xinyuedata.test_case.models.driver import browser

class Readerdata():
    #数据库操作
    def __init__(self):
        self.diseases = 0
        self.file = 0
        self.url = 0

     #读取病种
    def reader_diseases(self):
        #读取系统
        self.diseases = []
        list = parameter.read_csv('banner.csv')
        for data in islice(list,1,None):
            self.diseases.append(data[0])
        return  self.diseases

    #读取文件
    def reader_file(self):

        self.file = []
        list = parameter.read_csv('banner.csv')
        for data in islice(list,1,None):
            self.file.append(data[1])
        return  self.file

    #读取URL
    def reader_url(self):
        self.url = []
        list = parameter.read_csv('banner.csv')
        for data in islice(list,1,None):
            self.url.append(data[2])
        return  self.url

class operation(Banner):
    #操作活动
    def __init__(self,driver,diseases,filepath,url):
        self.driver =driver
        self.diseases = diseases
        self.filepath = filepath
        self.url = url

     #登陆

    def user_login_verify(self,username='admin',password='admin123'):
        login(self.driver).user_login(username,password)

    def iframe_verify(self):
         lebel = lebelingPage(self.driver)
         self.user_login_verify()
         lebel.learen_banner()

    #新增banne
    def new_banner_verify(self):
        self.iframe_verify()
        po = Banner(self.driver)
        po.new_banner_button()
        sleep(1)
        if self.diseases == '儿童孤独症':
            po.diseases_children()
        elif self.diseases == '双相情感障碍':
            po.diseases_affections()
        elif self.diseases == '强迫症':
            po.diseases_ocd()
        po.select_input(self.filepath)
        po.url_input(self.url)
        po.save_button()

    #改变停用按钮
    def state_verify(self):
        #self.iframe_verify()
        po = Banner(self.driver)
        po.stop_button()

    #修改banner
    def modification_verify(self):
        self.iframe_verify()
        po = Banner(self.driver)
        po.modification_button()
        sleep(1)
        if self.diseases == '儿童孤独症':
            po.diseases_children()
        elif self.diseases == '双相情感障碍':
            po.diseases_affections()
        elif self.diseases == '强迫症':
            po.diseases_ocd()
        po.select_input(self.filepath)
        po.url_input(self.url)
        po.save_button()



class Bannerdmin(myunit.MyTest):
       '''
       banner界面，验证
       '''
       #banner 版本功能验证
       def test_add1(self):

           r = Readerdata()
           op = operation(self.driver,
                          r.reader_diseases()[0],
                          r.reader_file()[0],
                          r.reader_url()[0]
                          )
           po = Banner(self.driver)
           op.new_banner_verify()
           sleep(3)
           title = po.title_alert(self.driver)
           self.assertEqual(title,'操作成功！')

      #病种为空

       #病种为空
       def test_add2(self):

           r = Readerdata()
           op = operation(self.driver,
                          r.reader_diseases()[1],
                          r.reader_file()[1],
                          r.reader_url()[1]
                          )
           po = Banner(self.driver)
           op.new_banner_verify()
           sleep(3)
           title = po.title_alert(self.driver)
           self.assertEqual(title,'请选择病种')

       #文件为空
       def test_add3(self):

           r = Readerdata()
           op = operation(self.driver,
                          r.reader_diseases()[2],
                          r.reader_file()[2],
                          r.reader_url()[2]
                          )
           po = Banner(self.driver)
           op.new_banner_verify()
           sleep(3)
           title = po.title_alert(self.driver)
           self.assertEqual(title,'目标连接不能为空')

       #url为空
       def test_add4(self):

           r = Readerdata()
           op = operation(self.driver,
                          r.reader_diseases()[3],
                          r.reader_file()[3],
                          r.reader_url()[3]
                          )
           po = Banner(self.driver)
           op.new_banner_verify()
           sleep(3)
           title = po.title_alert(self.driver)
           self.assertEqual(title,'目标连接不能为空')

       #选择其他病种
       def test_add5(self):

           r = Readerdata()
           op = operation(self.driver,
                          r.reader_diseases()[4],
                          r.reader_file()[4],
                          r.reader_url()[4]
                          )
           po = Banner(self.driver)
           op.new_banner_verify()
           sleep(3)
           title = po.title_alert(self.driver)
           self.assertEqual(title,'操作成功！')

       #选择其他图片
       def test_add6(self):

           r = Readerdata()
           op = operation(self.driver,
                          r.reader_diseases()[5],
                          r.reader_file()[5],
                          r.reader_url()[5]
                          )
           po = Banner(self.driver)
           op.new_banner_verify()
           sleep(3)
           title = po.title_alert(self.driver)
           self.assertEqual(title,'操作成功！')

       #改变banner状态
       def test_add7(self):
           r = Readerdata()
           op = operation(self.driver,
                          r.reader_diseases()[5],
                          r.reader_file()[5],
                          r.reader_url()[5]
                          )
           po = Banner(self.driver)
           op.iframe_verify()
           list = po.data_list()
           op.state_verify()
           po.title_alert(self.driver)
           list1 = po.data_list()
           self.assertNotEqual(list[3],list1[3])

       #修改操作
       def test_add8(self):
           r = Readerdata()
           op = operation(self.driver,
                          r.reader_diseases()[6],
                          r.reader_file()[6],
                          r.reader_url()[6]
                          )
           po = Banner(self.driver)
           op.modification_verify()
           sleep(3)
           title = po.title_alert(self.driver)
           self.assertEqual(title,'操作成功！')

       #查看目标网页
       def test_add9(self):
           r = Readerdata()
           op = operation(self.driver,
                          r.reader_diseases()[6],
                          r.reader_file()[6],
                          r.reader_url()[6]
                          )
           op.iframe_verify()
           sreach_windows = self.driver.current_window_handle
           op.target_url_button()
           all_handle = self.driver.current_window_handle
           print(sreach_windows,all_handle)
           sleep(10)
           function.inster_img(self.driver,'学习_banner_查看网页.jpg')

if __name__ == '__main__':
    unittest.main()