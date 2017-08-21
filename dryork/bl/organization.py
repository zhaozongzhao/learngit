def organization(driver,f):
     import time
     f.write('机构同步'+'\t')
     try:
       driver.find_element_by_xpath('//*[@id="nav"]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/div/div[1]').click()
       time.sleep(0.5)
       url=driver.current_url
       f.write(url+'\t')
       title=driver.title
       f.write(title+'\n')
       driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div/div[2]/button[2]/div/div').click()
       h=driver.find_element_by_xpath('/html/body/div[10]/div[1]/div/div[2]').text
       f.write(+h)
       print(h)
       driver.find_element_by_xpath('/html/body/div[10]/div[2]/div/button/div/div').click()
     except Exception as a:
        print(a)
     else:
         f.write('机构同步成功')
def delete(driver,f):
    import time
    print('删除分院')
    try:
        #删除分分院
     driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]').click()
     driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/div/div[1]/div[3]/div/div/div[2]/div[1]/div/div[1]').click()
     driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]').click()
     time.sleep(0.5)
     driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/button[3]').click()
     driver.find_element_by_xpath('/html/body/div[9]/div[2]/button[2]').click()

    except Exception as a:
        print(a)
    else:
        print('删除成功')