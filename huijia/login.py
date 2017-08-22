from selenium import  webdriver
driver=webdriver.Chrome()

def Driver():
    driver=webdriver.Chrome()
    return driver

def login(driver,name,password,mia):
    driver.get('http://hj.dryork.cn/huijia/admin/main')
    driver.find_element_by_xpath('//*[@id="userid"]').send_keys(name)
    driver.find_element_by_xpath('//*[@id="userpassid"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="checkNumber"]').send_keys(mia)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[3]/div[1]/div/div/form/fieldset/div[3]/button').click()
    w=driver.find_element_by_xpath('//*[@id="navbar-container"]/div[1]/a/small').text
    return w
def start(driver):
    login(driver)




















