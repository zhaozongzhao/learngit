import time
def  Card(driver):#预览医生名片
    time.sleep(2)
    driver.find_element_by_id('com.dentist.android:id/titleRightTv').click()
    driver.find_element_by_name('名片').click()
    time.sleep(5)
    driver.get_screenshot_as_file('F:/app/picture/1.jpg')

def Upder(driver):#修改医生名片
    driver.find_element_by_name('更多').click()
    driver.find_element_by_name('修改').click()
    driver.get_screenshot_as_file('F:/app/picture/修改名片.jpg')
    #名称修改
    driver.find_element_by_name('姓名').click()
    driver.find_element_by_id('com.dentist.android:id/inputEt').click()
    driver.find_element_by_id('com.dentist.android:id/inputEt').send_keys('赵宗召')
    driver.find_element_by_name('保存').click()
    #医院修改
    driver.find_element_by_name('医院').click()
    driver.find_element_by_id('com.dentist.android:id/hospitalEt').send_keys('北京建国医院')
    driver.find_element_by_name('返回').click()
    #科室修改
    driver.find_element_by_name('科室').click()
    driver.find_element_by_name('口腔综合科').clisk()
    #职称修改
    driver.find_element_by_name('职称').click()
    driver.find_element_by_name('主任医师').click()
    #保存修改
    driver.find_element_by_name('保存').click()
    driver.screenshor_as_file('F:/app/picture/保存名片.jpg')

def stype(driver):
     Card(driver)
    







