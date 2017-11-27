'''
创建页面基础类，通过_init_()方法初始化参数：浏览器驱动，url地址，超时时间。
定义基本方法:
  open()用于打开心悦地址，find_elements 和 find_element () 分别用来定位单个和多个元素，创建script（）方法可以用来更简便
  的调用JavaScript代码
'''
from selenium import webdriver


class Page(object):
    '''
    创建基础类用于所有页面的继承
    '''
    xinyue_url = 'http://xy.xinyuezx.cn/xinyue_manage/admin/main'

    def __init__(self,selenium_driver,base_url =xinyue_url ):
        self.base_uel =base_url
        self.driver = selenium_driver
        self.timeout = 30



    def find_element(self,*loc):
        '''
        定义单个元素
        '''
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        '''
        定义一组元素
        '''
        return  self.driver.find_elements(*loc)

    def on_page(self):
        #对url进行判断
        return self.driver.current_url == (self.base_uel+self.url)

    def _open(self,url):
        #实际打开url的操作
        url = self.base_uel+url
        self.driver.get(url)
        assert  self.on_page(),'没有这个url'

    def open(self):
        #用于打开Url
        self._open(self.url)

    def script(self,src):
        #更简便的调用JavaScriot代码.
        return self.driver.execute_script(src)



