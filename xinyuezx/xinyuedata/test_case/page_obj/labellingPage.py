from  selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.by import By
from xinyuedata.test_case.page_obj import base
from time import  sleep

class lebelingPage(base.Page):

    #学习管理场景
    learen_administer_loc = (By.XPATH,'//*[@id="menuDemo"]/li[2]/a/span')                         #学习管理
    learen_banner_loc = (By.XPATH,'//*[@id="menuDemo"]/li[2]/ul/li[1]/a/span')                   #banner
    learen_information_loc = (By.XPATH,'//*[@id="menuDemo"]/li[2]/ul/li[2]/a/span')              #资讯管理
    learen_guide_loc = (By.XPATH,'//*[@id="menuDemo"]/li[2]/ul/li[3]/a/span')                    #指南管理
    #定位学习管理，返回对象
    def learen_administer(self):
       self.find_element(*self.learen_administer_loc).click()

    #定位banner
    def learen_banner(self):
        self.learen_administer()
        self.find_element(*self.learen_banner_loc).click()
        self.driver.switch_to_frame('cframe')


    #定位资讯管理
    def learen_information(self):
        self.learen_administer()
        self.find_element(*self.learen_information_loc).click()
        self.driver.switch_to_frame('cframe')

    #定位指南管理
    def learen_guide(self):
        self.learen_administer()
        self.find_element(*self.learen_guide_loc).click()
        self.driver.switch_to_frame('cframe')