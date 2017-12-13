'''
创建截图函数inster_img(），为保持项目的可移植性，采用相对路径将截图保存在.\report\imsge目录中
'''

from selenium import webdriver
import os
#截图函数
def inster_img(driver,file_name):
    #获取当前目录
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    #将路径中的\\用\取代
    base_dir = base_dir.replace('\\','/')
    base = base_dir.split('/test_case')[0]
    file_path = base +'/report/image/'+file_name
    #截取当前窗口，并将图存储在当前位置
    #print(file_path)
    driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://xy.xinyuezx.cn/xinyue_manage/admin/main')
    inster_img(driver,'login.jpg')
    driver.quit()