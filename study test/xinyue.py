from selenium import  webdriver
from  time import sleep
from selenium.webdriver.common.by import By

class Page (object):
    '''基础类用于页面继承'''

    login_url = 'http://xy.dryork.cn/xinyue_manage/admin/main'


   #创建一个基础类page，在初始方法中定义驱动，基本的URL，和超时时间
    def __init__(self,selenium_webdriver,base_url=login_url):
        self.base_url=base_url
        self.driver=selenium_webdriver
        self.timeout=30

    #打开浏览器的操作
    def open(self):
        self._open(self.url)

    #实际打开浏览器的操作
    def _open(self,url):
         url=self.base_url+url
         self.driver.get(url)
         assert  self.on_page(),'没有咋样的url%s'%url

    #断言
    def on_page(self):
        return self.driver.current_url==(self.base_url+self.url)

    #定位
    def find_element(self,*loc):
        return self.driver.find_element(*loc)


class LoginPage(Page):
    #对象层
    '''心悦测试环境模拟'''
    url = ''

    #定位器
    uesename_loc=(By.ID,'userid')
    password_loc=(By.ID,'userpassid')
    submit_loc=(By.XPATH,'//*[@id="formid"]/fieldset/div[2]/button/span')

    #场景
    #登录用户，封装
    def type_username(self,username):
         self.find_element(*self.uesename_loc).send_keys(username)
    #登录密码 封装
    def type_password(self,password):
         self.find_element(*self.password_loc).send_keys(password)
    #登录按钮   封装
    def  submit(self):
        self.find_element(*self.submit_loc).click()


#将单个元素组成一个完整的动作，这个动作包含打开浏览器，输入用户名密码
def test_user_login(driver,username,password):
    '''测试获取的用户名、密码是否可以登录'''
    login_page=LoginPage(driver)
    login_page.open()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()


'''def main(name,passw):
    try:
        driver = webdriver.Chrome()
        username=name
        password=passw
        test_user_login(driver, username, password)
        sleep(3)
        text=driver.find_element_by_xpath('// *[ @ id = "navbar-container"] / div[1] / a / small').text
        assert (text=='心悦后台管理系统'),'用户名不匹配登录失败！'
    finally:
        #关闭浏览器
        sleep(3)
        driver.close()

def dd(driver):
    return driver'''






