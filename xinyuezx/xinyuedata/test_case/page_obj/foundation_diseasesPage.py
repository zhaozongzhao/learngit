from  selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.by import By
from xinyuedata.test_case.page_obj import base
from time import  sleep

class diseases(base.Page):
    '''系统管理 -知识库界面展示'''
    url = ''
    new_add_button_loc = (By.ID,'add-modal')#新增按钮
    Job_title_input_loc = (By.ID,'titlesName')#职称输入框
    Job_title_down_button_loc = (By.CLASS_NAME,'btn btn-default')#关闭按钮
    Job_title_save_button_loc =(By.XPATH,'/html/body/div[3]/div/div/div[3]/button[2]')#保存按钮
    Job_title_stop_loc =(By.XPATH,'//*[@id="recommend-table"]/tbody/tr[1]/td[4]/a')#列表第一个操作元素
    Job_title_list_loc = (By.CLASS_NAME,'pagination-info')#列表统计数据
    Job_title_type_loc = (By.XPATH,'//*[@id="recommend-table"]/tbody/tr[1]/td[3]')#列表第一个元素的状态

    def add_buutton(self):
        '''点击新增按钮'''
        self.find_element(*self.new_add_button_loc).click()

    def job_title_input(self,title):
        '''职称输入'''
        self.find_element(*self.Job_title_input_loc).send_keys(title)

    def down_button(self):
        '''关闭操作'''
        self.find_element(*self.Job_title_down_button_loc).click()

    def save_button(self):
        '''保存操作'''
        print('开始操作')
        self.find_element(*self.Job_title_save_button_loc).click()

    def stop_button(self):
        '''停用/启用操作'''
        self.find_element(*self.Job_title_stop_loc).click()

    def list_quantity(self):
        '''获取职称列表数量'''
        return  self.find_element(*self.Job_title_list_loc).text

    def type_state(self):
        '''查询元素状态'''
        return  self.find_element(*self.Job_title_type_loc).text

    def title_alert(self,driver):
        '''接收alert'''
        h=driver.switch_to_alert().text
        driver.switch_to_alert().dismiss()
        return  h







