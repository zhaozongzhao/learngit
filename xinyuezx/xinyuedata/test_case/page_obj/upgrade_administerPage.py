from  selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.by import By
from xinyuedata.test_case.page_obj import base
from time import  sleep

class upgrade(base.Page):
    '''
    升级管理界面，继承的界面类
    '''
    url = ''

    upgrade_administer_labelling_loc =(By.XPATH,'//*[@id="menuDemo"]/li[1]/ul/li[3]/a/span')#升级管理标签
    def upgrade_administer_labelling(self):
       #点击标签按钮
       self.find_element(*self.upgrade_administer_labelling_loc).click()


    #查询场景
    systems_input_loc = (By.ID,'clientPlat')#系统输入框
    clear_button_loc = (By.ID,'emptyCondition')#清空按钮
    enquiries_button_loc = (By.ID,'commitSearch')#查询按钮
    new_button_loc = (By.ID,'add-modal')#新增按钮

    #筛选系统
    def screening_system_input(self,system):

        self.find_element(*self.systems_input_loc).send_keys(system)

      #清空按钮

    #清空按钮
    def clear_button(self):
        self.find_element(*self.clear_button_loc).click()

     #查询按钮

    #查询按钮
    def enquires_button(self):
        self.find_element(*self.enquiries_button_loc).click()

    #新增按钮
    def new_button(self):
        self.find_element(*self.new_button_loc).click()

    #添加升级管理场景
    systems_select_loc = (By.ID,'clientPlatform')#系统多选框
    Version_number1_loc = (By.ID,'currVersion1')#版本1
    Version_number2_loc = (By.ID,'currVersion2')#版本2
    Version_number3_loc = (By.ID,'currVersion3')#版本3
    upgrade_headings_input_loc = (By.ID,'updateTitle')#升级管理标题
    upgrade_prompting_input_loc = (By.ID,'updateInfo')#升级提示
    upgrade_url_input_loc = (By.ID,'downloadUrl')#升级地址
    isupupgrade_input_loc = (By.XPATH,'//*[@id="isforce"]')#是否强制升级
    save_button_loc = (By.XPATH,'//*[@id="btn2"]')#新建确定按钮
    save_button_loc1 = (By.XPATH,'//*[@id="btn1"]')#修改确定按钮
    #系统选择框
    def system_input(self):

        system = self.find_element(*self.systems_select_loc)
        sleep(1)
        return system
    #选择ios系统
    def ios_system_input(self):

        system = self.system_input()
        system.find_element(By.XPATH,'//*[@id="clientPlatform"]/option[2]').click()
    #选择android
    def android_system_input(self):
        system = self.system_input()
        system.find_element(By.XPATH,'//*[@id="clientPlatform"]/option[3]').click()

    #版本输入框
    def Version_number_input(self,number1,number2,number3):

        self.find_element(*self.Version_number1_loc).send_keys(number1)
        self.find_element(*self.Version_number2_loc).send_keys(number2)
        self.find_element(*self.Version_number3_loc).send_keys(number3)

    #升级标题
    def upgrade_headings_input(self,headings):

        self.find_element(*self.upgrade_headings_input_loc).send_keys(headings)

    #升级提示
    def upgrade_prompting_input(self,prompting):

        self.find_element(*self.upgrade_prompting_input_loc).send_keys(prompting)

    #升级地址
    def upgrade_url_input(self,url):

        self.find_element(*self.upgrade_url_input_loc).send_keys(url)

    #是否强制升级
    def isupupgrade_input(self):

        self.find_element(*self.isupupgrade_input_loc).click()

    #点击保存
    def save_button(self):
        self.find_element(*self.save_button_loc).click()


    #列表场景
    list_data_table_loc =(By.XPATH,'//*[@id="recommend-table"]')#列表数据
    list_tr_object_loc = (By.TAG_NAME,'tr')#行对象
    list_td_object_loc = (By.TAG_NAME,'td')#列对象
    list_stop_button_loc = (By.XPATH,'//*[@id="recommend-table"]/tbody/tr[1]/td[8]/a[1]')#启用停用按钮
    list_modification_button_loc = (By.XPATH,'//*[@id="recommend-table"]/tbody/tr[1]/td[8]/a[2]')#修改按
    list_statistics_data_loc = (By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[4]/div[1]/span[1]')#统计数据

    #获取数据
    def list_data(self):
        list_data = []
        table = self.find_element(*self.list_data_table_loc)#获取页面对象
        sleep(0.3)
        trlist = table.find_elements(*self.list_tr_object_loc)#获取tr对象
        sleep(0.3)
        for row in trlist:
            #遍历每一行
            talis = row.find_elements(*self.list_td_object_loc)
            for col in talis:
              list_data.append(col.text)

        return list_data

    #接收提示语句
    def title_alert(self,driver):
        '''接收alert'''

        h=driver.switch_to_alert().text
        driver.switch_to_alert().dismiss()
        return  h

    #点击停用启用按钮
    def list_stop_button(self):
        self.find_element(*self.list_stop_button_loc).click()

    #点击修改按钮
    def list_modification_button(self):
        self.find_element(*self.list_modification_button_loc).click()

    #统计数据
    def list_statistics_data(self):
        self.find_element(*self.list_statistics_data_loc).click()

    #修改确定按钮
    def save_button1(self):

        self.find_element(*self.save_button_loc1).click()













