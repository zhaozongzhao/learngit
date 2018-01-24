from time import sleep
import unittest
from xinyuedata.test_case.models import myunit,function,parameter
from xinyuedata.test_case.page_obj import loginPage
from xinyuedata.test_case.page_obj.learn_guide_Page import Guide
from xinyuedata.test_case.page_obj.labellingPage import lebelingPage
from xinyuedata.test_case.page_obj.loginPage  import login
from itertools import islice
from xinyuedata.test_case.models.driver import browser


class Readerdata():
    '''读取数据操作'''
    #数据库操作
    def __init__(self):
        self.guidename = 0
        self.cover = 0
        self.remarks = 0
        self.introduce = 0
        self.directoryin = 0
        self.name = 0
        self.head = 0
        self.position = 0
        self.synopsis = 0
        self.remarks1 = 0

     #指南名称
    def reader_guidename(self):
        #读取系统
        self.guidename = []
        list = parameter.read_csv('learn_guide.csv')
        for data in islice(list,1,None):
            self.guidename.append(data[0])
        return  self.guidename

    #指南封面
    def reader_cover(self):
        #读取系统
        self.cover = []
        list = parameter.read_csv('learn_guide.csv')
        for data in islice(list,1,None):
            self.cover.append(data[1])
        return  self.cover

    #指南寄语
    def reader_remarks(self):
        #读取系统
        self.remarks = []
        list = parameter.read_csv('learn_guide.csv')
        for data in islice(list,1,None):
            self.remarks.append(data[2])
        return  self.remarks

     #指南目录
    def reader_introduce(self):
        #读取系统
        self.introduce = []
        list = parameter.read_csv('learn_guide.csv')
        for data in islice(list,1,None):
            self.introduce.append(data[3])
        return  self.introduce

    #指南介绍
    def reader_directoryin(self):
        #读取系统
        self.directoryin = []
        list = parameter.read_csv('learn_guide.csv')
        for data in islice(list,1,None):
            self.directoryin.append(data[4])
        return  self.directoryin

    #编者名称
    def reader_name(self):
        self.name = []
        list = parameter.read_csv('learn_guide.csv')
        for data in islice(list,1,None):
            self.name.append(data[5])
        return  self.name

    #编者头像
    def reader_head(self):
        self.head = []
        list = parameter.read_csv('learn_guide.csv')
        for data in islice(list,1,None):
            self.head.append(data[6])
        return  self.head

    #职务
    def reader_position(self):
        self.position = []
        list = parameter.read_csv('learn_guide.csv')
        for data in islice(list,1,None):
            self.position.append(data[7])
        return  self.position

    #编者简介
    def reader_synopsis(self):
        self.synopsis = []
        list = parameter.read_csv('learn_guide.csv')
        for data in islice(list,1,None):
            self.synopsis.append(data[8])
        return  self.synopsis

    #编者寄语
    def reader_remarks1(self):
        self.remarks1 = []
        list = parameter.read_csv('learn_guide.csv')
        for data in islice(list,1,None):
            self.remarks1.append(data[9])
        return  self.remarks1


class operation(Guide):
    '''界面操作类'''

    def __init__(self,driver):
        self.driver = driver

    #登录操作
    def user_login_verify(self,username='admin',password='admin123'):
        login(self.driver).user_login(username,password)

    #进入标签页
    def iframe_verify(self):
         lebel = lebelingPage(self.driver)
         self.user_login_verify()
         lebel.learen_guide()

    #新建指南
    def new_guide(self,name,cover,remarks,introduce,directoryin):
        self.iframe_verify()
        po = Guide(self.driver)
        po.modification_button()
        po.guide_name_button(name)
        po.guide_cover_input(cover)
        po.guide_remarks_inputs(remarks)
        po.guide_introduce_input(introduce)
        po.guide_directoryin_input(directoryin)
        po.save_button()

    def new_editor(self,name,head,position,synopsis,emarks):
        self.iframe_verify()
        po = Guide(self.driver)
        po.modification_button()
        po.new_editor_button()
        po.editor_name_input(name)
        po.editor_head_input(head)
        po.editor_position_input(position)
        po.editor_synopsis_input(synopsis)
        po.editor_remarks_input(emarks)
        po.editor_save_button()

class Guideadmin(myunit.MyTest):
    '''指南管理界面测试'''

    def test_new_guide(self):
        '''添加指南功能验证'''
        r = Readerdata()
        op = operation(self.driver)
        op.new_guide(r.reader_guidename()[0],
                     r.reader_cover()[0],
                     r.reader_remarks()[0],
                     r.reader_introduce()[0],
                     r.reader_directoryin()[0])
        sleep(1)
        self.assertEqual(op.title_alert(self.driver),'操作成功！')

    def test_new_guide_name_null(self):
        '''添加指南功能验证'''
        r = Readerdata()
        op = operation(self.driver)
        op.new_guide(r.reader_guidename()[1],
                     r.reader_cover()[1],
                     r.reader_remarks()[1],
                     r.reader_introduce()[1],
                     r.reader_directoryin()[1])
        sleep(1)
        self.assertEqual(op.title_alert(self.driver),'指南名称不能为空')


    def test_new_guide_introduce_null(self):
        '''添加指南功能验证'''
        r = Readerdata()
        op = operation(self.driver)
        op.new_guide(r.reader_guidename()[2],
                     r.reader_cover()[2],
                     r.reader_remarks()[2],
                     r.reader_introduce()[2],
                     r.reader_directoryin()[2])
        sleep(1)
        self.assertEqual(op.title_alert(self.driver),'请输入指南介绍')

    def test_new_guide_directoryin_null(self):
        '''添加指南功能验证'''
        r = Readerdata()
        op = operation(self.driver)
        op.new_guide(r.reader_guidename()[3],
                     r.reader_cover()[3],
                     r.reader_remarks()[3],
                     r.reader_introduce()[3],
                     r.reader_directoryin()[3])
        sleep(1)
        self.assertEqual(op.title_alert(self.driver),'操作成功！')

    def test_new_editor(self):
        '''添加编者验证'''
        r = Readerdata()
        op = operation(self.driver)
        op.new_editor(r.reader_name()[0],
                      r.reader_head()[0],
                      r.reader_position()[0],
                      r.reader_synopsis()[0],
                      r.reader_remarks1()[0])
        sleep(1)
        self.assertEqual(op.title_alert(self.driver),'操作成功！')

    def test_new_editor_name_null(self):
        '''添加编者验证'''
        r = Readerdata()
        op = operation(self.driver)
        op.new_editor(r.reader_name()[1],
                      r.reader_head()[1],
                      r.reader_position()[1],
                      r.reader_synopsis()[1],
                      r.reader_remarks1()[1])
        sleep(1)
        self.assertEqual(op.title_alert(self.driver),'编辑名称不能为空')

    def test_new_editor_head_null(self):
        '''头像不能为空'''
        r = Readerdata()
        op = operation(self.driver)
        op.new_editor(r.reader_name()[2],
                      r.reader_head()[2],
                      r.reader_position()[2],
                      r.reader_synopsis()[2],
                      r.reader_remarks1()[2])
        sleep(1)
        self.assertEqual(op.title_alert(self.driver),'缩略图不能为空')

    def test_new_editor_position_null(self):
        '''职务不能为空'''
        r = Readerdata()
        op = operation(self.driver)
        op.new_editor(r.reader_name()[3],
                      r.reader_head()[3],
                      r.reader_position()[3],
                      r.reader_synopsis()[3],
                      r.reader_remarks1()[3])
        sleep(1)
        self.assertEqual(op.title_alert(self.driver),'职务不能为空')

    def test_new_editor_synopsis_null(self):
        '''简介不能为空'''
        r = Readerdata()
        op = operation(self.driver)
        op.new_editor(r.reader_name()[4],
                      r.reader_head()[4],
                      r.reader_position()[4],
                      r.reader_synopsis()[4],
                      r.reader_remarks1()[4])
        sleep(1)
        self.assertEqual(op.title_alert(self.driver),'简介不能为空')

    def test_new_editor_remarks1_null(self):
        '''简介不能为空'''
        r = Readerdata()
        op = operation(self.driver)
        op.new_editor(r.reader_name()[5],
                      r.reader_head()[5],
                      r.reader_position()[5],
                      r.reader_synopsis()[5],
                      r.reader_remarks1()[5])
        sleep(1)
        self.assertEqual(op.title_alert(self.driver),'寄语不能为空')




if __name__ == '__main__':
    unittest.main()

