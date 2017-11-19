'''  汇率计算
     作者： 赵宗召
     版本：v3.0
     时间：2017.11.18
     新增功能：程序可以一直运行，直到用户关闭
'''
USD_VS_RMB = 6.67

currenct_str_value = input('请输入货币金额（退出请按Q ）:  ')

while currenct_str_value!='Q':
    unit = currenct_str_value[-3:]
    if unit=='CHN':
        rmb_str_value = currenct_str_value[:-3]
        rmb_value=eval(rmb_str_value)
        usd_value = rmb_value /USD_VS_RMB
        print('美金金额为： ',usd_value)
        currenct_str_value = input('请输入货币金额（退出请按Q ）:  ')
    elif unit=='USD':
        usd_str_value = currenct_str_value[:-3]
        usd_value=eval(usd_str_value)
        rmb_value=usd_value * USD_VS_RMB
        print('人民币的金额为： ',rmb_value)
        currenct_str_value = input('请输入货币金额（退出请按Q ）:  ')
    else:
        print('正在开发中')
        currenct_str_value = input('请输入货币金额（退出请按Q ）:  ')
print('程序退出')