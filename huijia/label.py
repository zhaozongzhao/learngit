import time
import csv
from itertools import islice

def add(driver,tag):#添加标签
    time.sleep(0.5)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[2]/a/span').click()
    driver.switch_to.frame('cframe')
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="showSave-btn"]').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="labelName"]').send_keys(tag)
    driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div/div[1]/div/div/div[2]/div[3]/div[2]/div/button').click()
    time.sleep(0.5)
    amount=driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[4]/div[1]/span[1]').text
    b=check(amount)
    return b
def check(amount):
    substr='共'
    l=amount.rfind(substr)
    h=amount[l+1:-3]
    w=h.strip().lstrip().rstrip(' ')
    sum=int(w)
    return sum
