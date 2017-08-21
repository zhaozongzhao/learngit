#体现管理
import time
def audit(driver):
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[6]/a/span').click()
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/ul/li[6]/ul/li[2]/a/span').click()
        driver.switch_to.frame("cframe")
        time.sleep(0.5)
        data=driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/table/tbody').text#获取列表的数据
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[6]/a[1]').click()
        driver.find_element_by_xpath('//*[@id="no_cert"]').click()#定位审核失败按钮
        driver.find_element_by_xpath('//*[@id="no_appointRemark"]').send_keys('审核失败原因')

