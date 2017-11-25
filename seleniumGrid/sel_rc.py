from selenium import webdriver

sel=selenium('192.168.177.225',4444,'C','http:/www.baidu.com')

sel.start()

sel.open('/')

sel.type('id=kw','selenium grid')

sel.click('id=su')
sel.wait_for_page_to_load('30000')

sel.stop()

