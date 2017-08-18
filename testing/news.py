def text(driver):
    driver.find_element_by_id('com.dentist.android:id/maskView').click()
    driver.find_element_by_id('com.dentist.android:id/msgEt').send_keys('你好')
    driver.find_element_by_id('com.dentist.android:id/faceIb').click()
    driver.find_element_by_name('发送').click()

def photo(driver):
    driver.find_element_by_id('com.dentist.android:id/faceIb').click()
