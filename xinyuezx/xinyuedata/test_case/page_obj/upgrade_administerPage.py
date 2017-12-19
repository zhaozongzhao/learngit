from  selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.common.by import By
from xinyuedata.test_case.page_obj import base
from time import  sleep

class upgrade(base.Page):
    '''
    升级管理界面，继承的界面类
    '''
    url = ''

    upgrade_administer_labelling_loc =(By.CLASS_NAME,'menu-text')#升级管理标签

    #查询场景
    systems_input_loc = (By.ID,'clientPlat')#系统输入框
    clear_button_loc = (By.ID,'emptyCondition')#清空按钮
    enquiries_button_loc = (By.ID,'commitSearch')#查询按钮
    new_button_loc = (By.ID,'add-modal')#新增按钮

    #添加升级管理场景
    systems_select_loc = (By.ID,'clientPlatform')#系统多选框
    upgrade_headings_input_loc = (By.ID,'updateTitle')#升级管理标题
    upgrade_prompting_input_loc = (By.ID,'updateInfo')#升级提示
    upgrade_url_input = (By.ID,'downloadUrl')#升级地址
    isupupgrade_input_loc = (By.ID,'isforce')#是否强制升级

    #列表场景
    list_data_table_loc =(By.XPATH,'//*[@id="recommend-table"]')#列表数据
    list_tr_object_loc = (By.TAG_NAME,'tr')#行对象
    list_td_object_loc = (By.TAG_NAME,'td')#列对象
    list_stop_button_loc = (By.XPATH,'//*[@id="recommend-table"]/tbody/tr[1]/td[8]/a[1]')#启用停用按钮
    list_modification_button_loc = (By.XPATH,'//*[@id="recommend-table"]/tbody/tr[1]/td[8]/a[2]')#修改按钮
    list_statistics_data_loc = (By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[4]/div[1]/span[1]')#统计数据








