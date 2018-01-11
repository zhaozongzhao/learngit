from  selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.by import By
from xinyuedata.test_case.page_obj import base
from time import  sleep

class Purchase(base.Page):
     '''指南申购界面'''

     #列表操作场景
     list_data_loc = (By.XPATH,'//*[@id="recommend-table"]')#定位列表对象
     list_tr_object_loc = (By.TAG_NAME,'tr')#行对象
     list_td_object_loc = (By.TAG_NAME,'td')#列对象

     #获取列表数据
     def data_list(self):
        #定义获取列表数据的组
        list_data = []
        #获取列表对象
        table = self.find_element(*self.list_data_loc)
        #获取夜对象
        trlist = table.find_elements(*self.list_tr_object_loc)
        for row  in trlist:
            tdlist = row.find_elements(*self.list_td_object_loc)
            for col in tdlist:
                list_data.append(col.text)

        return  list_data