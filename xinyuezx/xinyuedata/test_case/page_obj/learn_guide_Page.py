from  selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.by import By
from xinyuedata.test_case.page_obj import base
from time import  sleep

class Guide(base.Page):
    '''指南管理界面信息'''

    #添加指南按钮
    modification_button_loc = (By.XPATH,'//*[@id="recommend-table"]/tbody/tr[1]/td[3]/a')     #指南修改按钮
    guide_name_input_loc = (By.XPATH,'//*[@id="guideName"]')                                     #指南名称
    guide_cover_input_loc = (By.XPATH,'//*[@id="imgFile"]')                                      #指南封面
    guide_remarks_input_loc = (By.XPATH,'//*[@id="guideAbstractImg"]')                          #指南寄语
    guide_introduce_input_loc = (By.XPATH,'//*[@id="guideIntroduce"]')                          #指南介绍
    guide_directoryin_input_loc = (By.XPATH,'//*[@id="editor1"]')                                #指南目录
    save_button_loc = (By.XPATH,'//*[@id="add-guide-info-btns"]')                               #确定按钮

    #点击修改按钮
    def modification_button(self):
        self.find_element(*self.modification_button_loc).click()

    #指南名称输入
    def guide_name_button(self,guidename):
        self.find_element(*self.guide_name_input_loc).clear()
        self.find_element(*self.guide_name_input_loc).send_keys(guidename)

    #指南封面上传
    def guide_cover_input(self,coverpath):
        self.find_element(*self.guide_cover_input_loc).send_keys(coverpath)

    #指南寄语界面
    def guide_remarks_inputs(self,remarks):
        self.find_element(*self.guide_remarks_input_loc).send_keys(remarks)

    #指南目录
    def guide_directoryin_input(self,directoryin):
        self.find_element(*self.guide_directoryin_input_loc).clear()
        self.find_element(*self.guide_directoryin_input_loc).send_keys(directoryin)

    #指南介绍
    def guide_introduce_input(self,introduce):
        self.find_element(*self.guide_introduce_input_loc).clear()
        self.find_element(*self.guide_introduce_input_loc).send_keys(introduce)

    def save_button(self):
        self.find_element(*self.save_button_loc).click()


    #添加编者场景
    new_editor_button_loc = (By.XPATH,'//*[@id="add-modal"]')                   #新增编者按钮
    editor_name_input_loc = (By.XPATH,'//*[@id="editorName"]')                  #编者姓名
    editor_head_input_loc = (By.XPATH,'//*[@id="iconnImg"]')                    #医生头像
    editor_position_input_loc = (By.XPATH,'//*[@id="editorTitles"]')            #职务
    editor_synopsis_input_loc = (By.XPATH,'//*[@id="editorIntroduction"]')     #简介
    editor_remarks_input_loc = (By.XPATH,'//*[@id="editorMessage"]')            #寄语
    editor_save_button_loc = (By.XPATH,'//*[@id="add-guide-edit-btn"]')        #确定按钮

    #点击新增编者按钮
    def new_editor_button(self):
        self.find_element(*self.new_editor_button_loc).click()

    #添加编者姓名
    def editor_name_input(self,name):
        self.find_element(*self.editor_name_input_loc).send_keys(name)

    #上传医生头像
    def editor_head_input(self,head):
        self.find_element(*self.editor_head_input_loc).send_keys(head)

    #查看医生职务
    def editor_position_input(self,position):
        self.find_element(*self.editor_position_input_loc).send_keys(position)

    #输入简介
    def editor_synopsis_input(self,synopsis):
        self.find_element(*self.editor_synopsis_input_loc).send_keys(synopsis)

    #输入寄语
    def editor_remarks_input(self,remarks):
        self.find_element(*self.editor_remarks_input_loc).send_keys(remarks)

    def editor_save_button(self):
        self.find_element(*self. editor_save_button_loc).click()


     #列表操作场景
    list_data_loc = (By.XPATH,'//*[@id="recommend-table"]')#定位列表对象
    list_tr_object_loc = (By.TAG_NAME,'tr')#行对象
    list_td_object_loc = (By.TAG_NAME,'td')#列对象


     #获取列表数据
    def data_list(self):

        #定义获取列表数据的组
        list_data = []
        #获取列表对象
        table = self.find_element(*self.list_data_loc)
        #获取夜对象
        trlist = table.find_elements(*self.list_tr_object_loc)
        for row  in trlist:
            tdlist = row.find_elements(*self.list_td_object_loc)
            for col in tdlist:
                list_data.append(col.text)

        return  list_data

    def title_alert(self,driver):
        '''接收alert'''
        h=driver.switch_to_alert().text
        driver.switch_to_alert().dismiss()
        return  h