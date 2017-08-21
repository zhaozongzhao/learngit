def role(driver):
    from time import sleep
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[1]').click()
    driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/button[2]').click()
    driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/button[1]').click()
    driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div[1]/div/div/div/input').send_keys('test1')
    """inputs=driver.find_element_by_class_name('mu-checkbox')
    for i in inputs:
        if i.get_attribute("class"):
         i.click()
         sleep(0.5)"""
    driver.find_elements_by_xpath("/html/body/div[6]/div[1]/div/div[2]/div/div[1]/label[1]").click()