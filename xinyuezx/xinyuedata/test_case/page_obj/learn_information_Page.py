from  selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.by import By
from xinyuedata.test_case.page_obj import base
from time import  sleep

class Information(base.Page):
    '''资讯管理界面的界面类'''

    new_button_loc = (By.XPATH,'//*[@id="add-modal"]')#添加按钮
    diseases_select_input_loc = (By.XPATH,'//*[@id="diseaseId"]')#病种选择框
    select_input_loc = (By.XPATH,'//*[@id="imgFile"]')#图片选择
    headings_input_loc = (By.XPATH,'//*[@id="title"]')#标题
    abstracts_input_loc = (By.XPATH,'//*[@id="abstracts"]')#摘要
    content_input_loc = (By.XPATH,'//*[@id="editor1"]')#资讯内容
    save_button_loc = (By.XPATH,'//*[@id="add-docadvice-btn"]')#保存按钮

    #添加按钮
    def new_button(self):
        self.find_element(*self.new_button_loc).click()


   #选择病种
    def diseases_select_input(self):
        diseases=self.find_element(*self.diseases_select_input_loc)
        return  diseases

    #儿童孤独症
    def diseases_children(self):
        diseases = self.diseases_select_input()
        diseases.find_element(By.XPATH,'//*[@id="diseaseId"]/option[4]').click()

    #选择病种
    def diseases_select_input(self):
        diseases=self.find_element(*self.diseases_select_input_loc)
        return  diseases

    #儿童孤独症
    def diseases_children(self):
        diseases = self.diseases_select_input()
        diseases.find_element(By.XPATH,'//*[@id="diseaseId"]/option[4]').click()


     #选择上传图片
    def select_input(self,filename):
        self.find_element(*self.select_input_loc).send_keys(filename)

    #输入标签
    def headings_input(self,headings):
        self.find_element(*self.headings_input_loc).clear()
        self.find_element(*self.headings_input_loc).send_keys(headings)

    #输入摘要
    def abstracts_input(self,abstracts):
        self.find_element(*self.abstracts_input_loc).clear()
        self.find_element(*self.abstracts_input_loc).send_keys(abstracts)

    #富文本输入
    def content_input(self,content):
        self.find_element(*self.content_input_loc).clear()
        self.find_element(*self.content_input_loc).send_keys(content)

    #保存按钮
    def save_button(self):
        self.find_element(*self.save_button_loc).click()


    #列表操作场景
    list_data_loc = (By.XPATH,'//*[@id="recommend-table"]')#定位列表对象
    list_tr_object_loc = (By.TAG_NAME,'tr')#行对象
    list_td_object_loc = (By.TAG_NAME,'td')#列对象
    stop_button_loc = (By.XPATH,'//*[@id="recommend-table"]/tbody/tr[1]/td[5]/a[1]')#停用按钮
    modification_button_loc = (By.XPATH,'//*[@id="recommend-table"]/tbody/tr[1]/td[5]/a[2]')#修改按钮statr

   #点击停用按钮
    def stop_button(self):
        self.find_element(*self.stop_button_loc).click()


    #点击修改按钮
    def modification_button(self):
        self.find_element(*self.modification_button_loc).click()


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


