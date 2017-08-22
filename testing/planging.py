def find(driver):

  driver.find_element_by_id('com.dentist.android:id/findBt').click()#进入发现界面
  driver.find_element_by_name('舒适种植').click()
  plan(driver)

def plan(driver):
    driver.find_element_by_name('方案管理').click()
    driver.find_element_by_id('com.dentist.android:id/titleRightTv').click()


def  user(driver):
    driver.get_name(driver,'选择患者').click()
    driver.get_name(driver,'总校').click()

def system(driver):
    

 def get_name(driver, name):
    element = driver.find_element_by_name(name)
    return element
