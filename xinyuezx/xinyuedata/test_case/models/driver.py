'''
定义浏览器函数browser()，该函数可以进行配置，根据我们的需求，配置测试用例在不同的主机及浏览器下运行
'''


from selenium.webdriver import Remote
from selenium import webdriver

#启动浏览器
def browser():
    driver = webdriver.Chrome()
    return driver

if __name__ == '__main__':

    dr = browser()
    dr.get('http://xy.xinyuezx.cn/xinyue_manage/admin/main')
    dr.quit()