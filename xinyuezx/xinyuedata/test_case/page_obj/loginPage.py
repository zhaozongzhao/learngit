'''
创建登陆页面对象，对用户登陆面上用户名/密码，登陆按钮和提示信息等元素的定位进行封装，除此之外，还创建user_login（）方法
作为系统统一登陆入口，关于对操作步骤的封装可以放在Page Object当中，主要考虑还有其他模块会调用该登陆方法，为username 和p
password 入参设置了默认值是为了方便其他用例在调用user_login()是不用再传递登陆用户信息，因为该系统大多数用例的执行使用该
账号即可，同时也方便了在账号失效时的修改
'''
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from xinyuedata.test_case.page_obj.base import Page
class login(Page):
    '''
    用户登陆界面
    '''
    url = ''
    #场景
    xinyue_login_user_loc = (By.XPATH,'//*[@id="userid"]')
    xinyue_login_password_loc = (By.XPATH,'//*[@id="userpassid"]')
    xinyue_login_button_loc = (By.XPATH,'//*[@id="formid"]/fieldset/div[2]/button')


    #登陆用户名
    def login_username(self,username):
        self.find_element(*self.xinyue_login_user_loc).send_keys(username)

    #登陆密码
    def login_password(self,password):
        self.find_element(*self.xinyue_login_password_loc).send_keys(password)

    #登陆按钮
    def login_button(self):
        self.find_element(*self.xinyue_login_button_loc).click()

     #定义统一登陆入口

    def user_login(self,username='admin',password='admin123'):
        '''
        获取的用户名密码登陆
        '''
        self.open()
        self.login_username(username)
        self.login_password(password)
        sleep(1)
        self.login_button()
        sleep(3)

    #用戶錯誤提示
    def user_error_hini(self,driver):

      h=driver.switch_to_alert().text
      driver.switch_to_alert().dismiss()
      return  h

    def alert_dimiss(self,driver):

        driver.switch_to_alert


    user_login_success_loc = (By.XPATH,'//*[@id="navbar-container"]/div[1]/a/small')

    #登陆成功
    def user_login_success(self):

        return self.find_element(*self.user_login_success_loc).text


