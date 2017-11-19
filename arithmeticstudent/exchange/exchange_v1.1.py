'''  汇率计算
     作者： 赵宗召
     版本：v1.1
'''
#汇率
USD_VS_RMB = 6.77#大写的参数表示不会轻易改变

kind_str_value = input('请选择货币种类 ：1.人民币 2.美金')

if  kind_str_value=='1':
    rmb_str_value = input('请输入人民币金额：')
    rmb_value = eval(rmb_str_value)#将string转化为数字
    usd_value = rmb_value / USD_VS_RMB#汇率计算
    print('美元金额： ' , usd_value)
elif kind_str_value=='2':
    rmb_str_value = input('请输入美金金额： ')
    rmb_value = eval(rmb_str_value)
    usd_value = rmb_value * USD_VS_RMB
    print('人民币金额： ', usd_value)