
'''  汇率计算
     作者： 赵宗召
     版本：v1.0
'''
#汇率
USD_VS_RMB = 6.77#大写的参数表示不会轻易改变

rmb_str_value = input('请输入人民币金额：')
rmb_value = eval(rmb_str_value)#将string转化为数字

usd_value = rmb_value / USD_VS_RMB#汇率计算
print('美元金额： ' , usd_value)