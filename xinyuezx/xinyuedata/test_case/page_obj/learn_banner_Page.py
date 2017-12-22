from  selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.by import By
from xinyuedata.test_case.page_obj import base
from time import  sleep

class Banner(base.Page):
    '''BANNER管理'''

    url = ''

   #新增场景
    new_banner_button_loc = (By.XPATH,'//*[@id="add-modal"]')#新增按钮
    diseases_select_input_loc = (By.XPATH,'//*[@id="diseaseId"]')#病种选择框
    select_input_loc = (By.XPATH,'//*[@id="imgFile"]')#图片选择
    url_input_loc = (By.XPATH,'//*[@id="gotoUrl"]')#url输入框
    save_button_loc = (By.XPATH,'//*[@id="add-docadvice-btn"]')#保存按钮
    cancel_button_loc = (By.XPATH,'//*[@id="guanbi2"]')#取消按钮

    #点击新增banner
    def new_banner_button(self):
        self.find_element(*self.new_banner_button_loc).click()

    #选择病种
    def diseases_select_input(self):
        diseases=self.find_element(*self.diseases_select_input_loc)
        return  diseases

    #儿童孤独症
    def diseases_children(self):
        diseases = self.diseases_select_input()
        diseases.find_element(By.XPATH,'//*[@id="diseaseId"]/option[4]').click()

    #双相情感障碍
    def diseases_affections(self):
        diseases = self.diseases_select_input()
        diseases.find_element(By.XPATH,'//*[@id="diseaseId"]/option[6]').click()

    #强迫症
    def diseases_ocd(self):
        diseases = self.diseases_select_input()
        diseases.find_element(By.XPATH,'//*[@id="diseaseId"]/option[9]').click()

    #选择上传图片
    def select_input(self,filename):
        self.find_element(*self.select_input_loc).send_keys(filename)

    #选择url
    def url_input(self,url):
        self.find_element(*self.url_input_loc).send_keys(url)

     #点击保存按钮
    def save_button(self):
        self.find_element(*self.save_button_loc).click()

    #点击取消按钮
    def cancel_button(self):
        self.find_element(*self.cancel_button_loc).click()



    #列表操作场景
    stop_button_loc = (By.XPATH,'//*[@id="recommend-table"]/tbody/tr[1]/td[5]/a[1]')#停用按钮
    modification_button_loc = (By.XPATH,'//*[@id="recommend-table"]/tbody/tr[1]/td[5]/a[2]')#修改按钮
    target_url_button_loc = (By.XPATH,'//*[@id="recommend-table"]/tbody/tr[1]/td[5]/a[3]')#查看目标网页
    list_data_loc = (By.XPATH,'//*[@id="recommend-table"]')#定位列表对象
    list_tr_object_loc = (By.TAG_NAME,'tr')#行对象
    list_td_object_loc = (By.TAG_NAME,'td')#列对象

    #点击停用按钮
    def stop_button(self):
        self.find_element(*self.stop_button_loc).click()


    #点击修改按钮
    def modification_button(self):
        self.find_element(*self.modification_button_loc).click()


    #点击查看目标网页

    def target_url_button(self):
        self.find_element(*self.target_url_button_loc).click()


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











