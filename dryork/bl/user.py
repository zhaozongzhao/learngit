def user(driver):
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div[1]').click()
    driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/button[1]').click()
    driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[1]/div[1]/div/div/input').send_keys('test1')
    driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[1]/div[2]/div/div/input').send_keys('111111')
    driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[2]/div[1]/div/div/input').send_keys('136@qq.com')
    driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[2]/div[2]/div/div/input').send_keys('13012345678')
    driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/button[1]').click()