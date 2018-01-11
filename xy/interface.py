from selenium import  webdriver
import tkinter
import tkinter.messagebox
import sys
sys.setrecursionlimit(1500)
from threading import Timer
import time

def code(driver):
    vc = driver.find_element_by_xpath('//*[@id="checkNumber"]').get_attribute('value')
    print(vc)
    if len(vc) >=4:
           driver.find_element_by_xpath('//*[@id="formid"]/fieldset/div[3]/button/span').click()

    else:
           time.sleep(5)
           code(driver)


def login():
    driver = webdriver.Chrome()
    driver.get('http://tempmanage.dryork.cn/yueke/admin/main')
    driver.find_element_by_xpath('//*[@id="userid"]').send_keys('admin')
    driver.find_element_by_xpath('//*[@id="userpassid"]').send_keys('admin123')


def judge(driver):
   driver.refresh()
   driver.switch_to_frame('cframe')
   time.sleep(3)
   h = driver.find_element_by_xpath('//*[@id="recommend-table"]/tbody/tr[1]/td[3]').text

   if h == '已启用':
       print('点击')
       driver.find_element_by_xpath('//*[@id="recommend-table"]/tbody/tr[1]/td[4]/a').click()
       driver.switch_to_alert().dismiss()
       return True
   else:
       print('点击')
       driver.find_element_by_xpath('//*[@id="recommend-table"]/tbody/tr[1]/td[4]/a').click()
       driver.switch_to_alert().dismiss()
       return False

def operation(driver):

       if judge(driver):
          print('开始')
          root = tkinter.Tk()
          top = tkinter
          top.messagebox.askokcancel('提示', '存在患者需要处理')
          root.destroy()
          print('结束')
       else:
        print('没有患者')
       t = Timer(10, operation(driver))
       t.start()

def main():
     driver =login()




if __name__ == '__main__':
    main()