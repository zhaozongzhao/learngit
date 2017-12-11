'''
病种管理
'''
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from xinyuedata.test_case.page_obj.base import Page

class entity(Page):
    url = ''
    labelling_button_loc = (By.XPATH,'//*[@id="menuDemo"]/li[1]/ul/li[1]/a/span')#病种管理标签
    new_add_button_loc = (By.ID,'add-modal')#新增病种
    entity_input_loc = (By.ID,'diseaseName')#病种名称
    show_input_loc = (By.XPATH,'//*[@id="checktwo"]')#是否显示勾选框
    confirm_button_loc = (By.ID,'btn2')#确定按钮
    cancel_button_loc = (By.ID,'guanbi2')#取消按钮
    list_data_loc = (By.XPATH,'/html/body/div[2]/div/div/div[2]/div[1]/div[2]/div[4]/div[1]/span[1]')#列表数据
    stop_button_loc = (By.XPATH,'//*[@id="recommend-table"]/tbody/tr[1]/td[5]/a[1]')#停用
    modification_button_loc = (By.XPATH,'//*[@id="recommend-table"]/tbody/tr[1]/td[5]/a[2]')#修改
    topper_button_loc = (By.XPATH,'//*[@id="recommend-table"]/tbody/tr[1]/td[5]/a[3]')#置顶按钮
    Moveup_button_loc = (By.XPATH,'//*[@id="recommend-table"]/tbody/tr[1]/td[5]/a[4]')#上移按钮
    Movedown_button_loc = (By.XPATH,'//*[@id="recommend-table"]/tbody/tr[1]/td[5]/a[5]')#下移按钮
    putthetail_button_loc = (By.XPATH,'//*[@id="recommend-table"]/tbody/tr[1]/td[5]/a[6]')#置尾按钮
    acquiring_button_loc = (By.XPATH,'//*[@id="recommend-table"]/tbody/tr[1]/td[2]')#病种名称

    #点击标签
    def labelling_button(self):
         self.find_element(*self.labelling_button_loc).click()

    #点击新增按钮
    def add_button(self):
        self.find_element(*self.new_add_button_loc).click()

    #病中数据输入
    def entity_input(self,entity):
        self.find_element(*self.entity_input_loc).send_keys(entity)

    #是否首页显示
    def show_click(self):
        self.find_element(*self.show_input_loc).click()

    #点击确认按钮
    def save_button(self):
        self.find_element(*self.confirm_button_loc).click()


    #点击取消按钮
    def cancel_button(self):
        self.find_element(*self.cancel_button_loc).click()

    #获取列表数据
    def list_data(self):
        self.find_element(*self.list_data_loc).text

    #点击停用按钮
    def stop_button(self):
        self.find_element(*self.stop_button_loc).click()

    #修改按钮
    def modification_button(self):
        self.find_element(*self.modification_button_loc).click()

    #置顶按钮
    def topper_button(self):
        self.find_element(*self.topper_button_loc).click()

    #上移按钮
    def Moveup_button(self):
        self.find_element(*self.Moveup_button_loc).click()

    #下移按钮
    def Movedown_button(self):
        self.find_element(*self.Movedown_button_loc).click()

    #置尾按钮
    def putthetail_button(self):
        self.find_element(*self.putthetail_button_loc).click()

    #获取病种
    def acquiring_button(self):
        self.find_element(*self.acquiring_button_loc).text


    def title_alert(self,driver):
        '''接收alert'''
        h=driver.switch_to_alert().text
        driver.switch_to_alert().dismiss()
        return  h















