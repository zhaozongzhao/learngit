from time import sleep
import unittest
from xinyuedata.test_case.models import myunit,function,parameter
from xinyuedata.test_case.page_obj import loginPage
from xinyuedata.test_case.page_obj.learn_information_Page import Information
from xinyuedata.test_case.page_obj.labellingPage import lebelingPage
from xinyuedata.test_case.page_obj.loginPage  import login
from itertools import islice
from xinyuedata.test_case.models.driver import browser

class Readerdata():
    '''读取数据操作'''
    #数据库操作
    def __init__(self):
        self.diseases = 0
        self.file = 0
        self.headings = 0
        self.abstracts = 0
        self.content = 0

     #读取病种
    def reader_diseases(self):
        #读取系统
        self.diseases = []
        list = parameter.read_csv('information.csv')
        for data in islice(list,1,None):
            self.diseases.append(data[0])
        return  self.diseases

    #读取文件
    def reader_file(self):

        self.file = []
        list = parameter.read_csv('information.csv')
        for data in islice(list,1,None):
            self.file.append(data[1])
        return  self.file

    #读取标签
    def reader_heading(self):
        self.headings = []
        list = parameter.read_csv('information.csv')
        for data in islice(list,1,None):
            self.headings.append(data[2])
        return  self.headings


    #读取摘要
    def reader_abstracts(self):
        self.abstracts = []
        list = parameter.read_csv('information.csv')
        for data in islice(list,1,None):
            self.abstracts.append(data[3])
        return  self.abstracts

    #读取内容
    def reader_content(self):
        self.content = []
        list = parameter.read_csv('information.csv')
        for data in islice(list,1,None):
            self.content.append(data[4])
        return  self.content

class operation(Information):
    '''资讯管理界面操作'''
    def __init__(self,driver):
        self.driver = driver


    #登录操作
    def user_login_verify(self,username='admin',password='admin123'):
        login(self.driver).user_login(username,password)

    #进入标签页
    def iframe_verify(self):
         lebel = lebelingPage(self.driver)
         self.user_login_verify()
         lebel.learen_information()

    #新增banne
    def new_banner_verify(self,diseases,filepath,headings,abstracts,content):
        self.iframe_verify()
        po = Information(self.driver)
        po.new_button()
        sleep(1)
        if diseases == '儿童孤独症':
            po.diseases_children()
        elif diseases == '双相情感障碍':
            po.diseases_affections()
        elif diseases == '强迫症':
            po.diseases_ocd()
        else:
            pass
        po.select_input(filepath)
        po.headings_input(headings)
        po.abstracts_input(abstracts)
        po.content_input(content)
        po.save_button()

    #改变停用按钮
    def state_verify(self):
        #self.iframe_verify()
        po = Information(self.driver)
        po.stop_button()

    #修改banner
    def modification_verify(self,diseases,filepath,headings,abstracts,content):
        self.iframe_verify()
        po = Information(self.driver)
        po.new_banner_button()
        sleep(1)
        if diseases == '儿童孤独症':
            po.diseases_children()
        elif diseases == '双相情感障碍':
            po.diseases_affections()
        elif diseases == '强迫症':
            po.diseases_ocd()
        po.select_input(filepath)
        po.headings_input(headings)
        po.abstracts_input(abstracts)
        po.content_input(content)
        po.save_button()

class Informationadmin(myunit.MyTest):
    '''资讯管理界面功能测试'''

    #基本功能验证
    def test_add1(self):
        r = Readerdata()
        op = operation(self.driver)
        op.new_banner_verify(r.reader_diseases()[0],
                             r.reader_file()[0],
                             r.reader_heading()[0],
                             r.reader_abstracts()[0],
                             r.reader_content()[0]
                             )
        sleep(1)
        title = op.title_alert(self.driver)
        self.assertEqual(title,'操作成功！')

    def test_add_diseases_null(self):
         r = Readerdata()
         op = operation(self.driver)
         op.new_banner_verify(r.reader_diseases()[1],
                             r.reader_file()[1],
                             r.reader_heading()[1],
                             r.reader_abstracts()[1],
                             r.reader_content()[1]
                             )
         sleep(1)
         title = op.title_alert(self.driver)
         self.assertEqual(title,'病种不能为空')


    def test_add_filepath_null(self):
         r = Readerdata()
         op = operation(self.driver)
         op.new_banner_verify(r.reader_diseases()[2],
                             r.reader_file()[2],
                             r.reader_heading()[2],
                             r.reader_abstracts()[2],
                             r.reader_content()[2]
                             )
         sleep(1)
         title = op.title_alert(self.driver)
         self.assertEqual(title,'图片不能为空')

    def test_add_hesding_null(self):
         r = Readerdata()
         op = operation(self.driver)
         op.new_banner_verify(r.reader_diseases()[3],
                             r.reader_file()[3],
                             r.reader_heading()[3],
                             r.reader_abstracts()[3],
                             r.reader_content()[3]
                             )
         sleep(1)
         title = op.title_alert(self.driver)
         self.assertEqual(title,'标题不能为空')


    def test_add_abstracts_null(self):
         r = Readerdata()
         op = operation(self.driver)
         op.new_banner_verify(r.reader_diseases()[4],
                             r.reader_file()[4],
                             r.reader_heading()[4],
                             r.reader_abstracts()[4],
                             r.reader_content()[4]
                             )
         sleep(1)
         title = op.title_alert(self.driver)
         self.assertEqual(title,'摘要不能为空')

if __name__ == '__main__':
    unittest.main()