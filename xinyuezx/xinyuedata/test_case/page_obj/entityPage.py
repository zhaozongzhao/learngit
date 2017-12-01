'''
病种管理
'''
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from xinyuedata.test_case.page_obj.base import Page

class entity(Page):
    url = ''
    new_add_button_loc = (By.ID,'add-modal')
    entity_input_loc = (By.ID,'diseaseName')
    show_input_loc = (By.id,'checktwo')
    confirm_button_loc = (By.ID,'btn2')
    cancel_button_loc = (By.ID,'guanbi2')
    list_data_loc = (By.XPATH,'/html/body/div[2]/div/div/div[2]/div[1]/div[2]/div[4]/div[1]/span[1]')
    stop_button_loc = (By.XPATH,'//*[@id="recommend-table"]/tbody/tr[1]/td[5]/a[1]')#停用


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


    def title_alert(self,driver):
        '''接收alert'''
        h=driver.switch_to_alert().text
        driver.switch_to_alert().dismiss()
        return  h















