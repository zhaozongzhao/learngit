'''  汇率计算
     作者： 赵宗召
     版本：v2.0
     新增功能：根据输入金额判断是人民币还是美元，进行汇率计算
'''
#汇率
USD_VS_RMB = 6.77#大写的参数表示不会轻易改变
#带单位的货币输入
currency_str_value = input('请输入带带单位的金额： ')
unit = currency_str_value[-3:]
if unit == 'CHN':
    rmb_str_value = currency_str_value[0:-3]
    rmb_value = eval(rmb_str_value)  # 将string转化为数字
    usd_value = rmb_value / USD_VS_RMB  # 汇率计算
    print('美元金额： ', usd_value)
elif unit == 'USD':
    usd_str_value = currency_str_value[0:-3]
    usd_value = eval(usd_str_value)  # 将string转化为数字
    rmb_value = usd_value * USD_VS_RMB  # 汇率计算
    print('人民币金额： ', rmb_value)
else:
    print('暂不支持其他货币计算')