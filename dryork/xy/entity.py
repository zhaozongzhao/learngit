import csv
from itertools import islice
#病种管理
import UCFilter
def add (driver,f):
    try:
      entity_reader = csv.reader(open('C:\\testing\\xy\\wpsc\\entity.csv','r'))
      from time import sleep
      f.write('添加病种\n')
      url=driver.current_url
      f.write(url+'\t')
      test=driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[1]/ul/li[1]/a/span').text
      f.write(test+'\n')
      sleep(0.5)
      for row in islice(entity_reader,1,None):
        driver.refresh()
        sleep(0.5)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[1]/ul/li[1]/a/span').click()
        driver.switch_to.frame("cframe")
        sleep(0.5)
        driver.find_element_by_xpath('//*[@id="add-modal"]').click()
        sleep(0.5)
        driver.find_element_by_xpath('//*[@id="diseaseName"]').send_keys(row)
        driver.find_element_by_xpath('//*[@id="checktwo"]').click()
        sleep(0.5)
        n=0
        w='C:\\testing\\xy\\wpsc\\添加病种'+str(n)+'.jgp'
        driver.get_screenshot_as_file(n)
        n=n+1
        driver.find_element_by_xpath('//*[@id="btn2"]').click()
        sleep(0.5)
        test1=driver.switch_to_alert().text
        f.write('\n\t'+test1)
        driver.switch_to_alert().dismiss()
    except Exception as s:
      print(s)


def Delete(driver,f):
  from time import sleep
  f.write('\t\t\n删除病种\n')
  driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[1]/ul/li[1]/a/span').click()
  driver.switch_to.frame("cframe")
  UCFilter.Title(driver)





