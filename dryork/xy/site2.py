#多点执业场所管理

def add(driver):
    import csv
    from time import sleep
    from itertools import islice
    See=csv.reader(open('C:\\testing\\xy\\wpsc\\site.csv','r'))
    for x in islice(See,1,None):
       name=x[0]
       site=x[3]
       Attn=x[4]
       phone=x[5]
       content=x[6]
       driver.refresh()
       sleep(0.5)
       driver.find_element_by_xpath('//*[@id="menuDemo"]/li[3]/a/span').click()
       sleep(0.5)
       driver.find_element_by_xpath('//*[@id="menuDemo"]/li[3]/ul/li[3]/a/span').click()
       driver.switch_to.frame("cframe")
       sleep(0.5)
       driver.find_element_by_xpath('//*[@id="add-modal"]').click()
       sleep(0.5)
       driver.find_element_by_xpath('//*[@id="names"]').send_keys(name)
       province=driver.find_element_by_xpath('//*[@id="province"]')
       province.find_element_by_xpath('//*[@id="province"]/option[5]').click()
       city=driver.find_element_by_xpath('//*[@id="city"]')
       city.find_element_by_xpath('//*[@id="city"]/option').click()
       driver.find_element_by_xpath('//*[@id="addresss"]').send_keys(site)
       driver.find_element_by_xpath('//*[@id="contactName"]').send_keys(Attn)
       driver.find_element_by_xpath('//*[@id="contactMobile"]').send_keys(phone)
       driver.find_element_by_xpath('//*[@id="editor1"]').send_keys(content)
       driver.find_element_by_xpath('//*[@id="statuss1"]').click()
       driver.find_element_by_xpath('//*[@id="add-docadvice-btn"]').click()
       sleep(0.5)
       driver.switch_to_alert().dismiss()
