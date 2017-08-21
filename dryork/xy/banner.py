from time import sleep
import csv
from itertools import islice
def add(driver,f):
        bann=csv.reader(open('C:\\testing\\xy\\wpsc\\banner.csv','r'))
        i=0
        for x in islice(bann,1,None):
          h=x[0]
          driver.refresh()
          driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[2]/a').click()
          sleep(0.5)
          driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[2]/ul/li[1]/a/span').click()
          driver.switch_to.frame('cframe')
          sleep(0.6)
          driver.find_element_by_xpath('//*[@id="add-modal"]').click()
          sleep(0.5)
          entity=driver.find_element_by_xpath('//*[@id="diseaseId"]')
          entity.find_element_by_xpath('%s'%h).click()
          driver.find_element_by_xpath('//*[@id="icon"]').send_keys('C:/testing/1.jpg')
          driver.find_element_by_xpath('//*[@id="gotoUrl"]').send_keys('http://download.csdn.net/download/wl520a/9748152')
          print('kaishi'+str(i))
          n='C:\\testing\\xy\\wpsc\\'+str(i)+'.jgp'
          i=i+1
          print(i)
          driver.get_screenshot_as_file(n)
          driver.find_element_by_xpath('//*[@id="add-docadvice-btn"]').click()
          text=driver.switch_to_alert().text
          print(text)

          driver.switch_to_alert().dismiss()





