
#专家
from time import sleep
def Add(driver):
    driver.refresh()
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[2]/a/span').click()
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[2]/ul/li[5]/a/span').click()
    driver.switch_to.frame('cframe')
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[3]/a').click()
    driver.find_element_by_xpath('//*[@id="add-modal"]').click()
    sleep(0.6)
    driver.find_element_by_xpath('//*[@id="expertName"]').send_keys('医生名称')
    driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/form/div[2]/div/input').send_keys('C:/testing/1.jpg')
    driver.find_element_by_xpath('//*[@id="expertTitles"]').send_keys('任职')
    driver.find_element_by_xpath('//*[@id="expertHospital"]').send_keys('医院')
    driver.find_element_by_xpath('//*[@id="expertIntroduction"]').send_keys('简介')
    driver.find_element_by_xpath('//*[@id="add-docadvice-btn"]').click()
    sleep(0.5)
    driver.switch_to_alert().dismiss()
