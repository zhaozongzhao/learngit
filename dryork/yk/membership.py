from selenium.common.exceptions import NoSuchElementException
def  manage(driver,f):
    driver.find_elements_by_xpath('/html/body/div[2]/div[1]/ul/li[13]/a/span').click()
    driver.find_elements_by_xpath('/html/body/div[2]/div[1]/ul/li[13]/ul/li[1]/a/span').click()
    driver.switch_to.frame('cframe')
def  statistics(driver,f):
    print()