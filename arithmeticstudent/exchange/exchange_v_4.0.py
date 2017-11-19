'''  汇率计算
     作者： 赵宗召
     版本：v4.0
     时间：2017.11.18
     新增功能：程序可以一直运行，直到用户关闭
     v4.0 将兑换功能封装成函数

'''

def conver_currenct(money,exchange):
    '''对于兑换金额的计算'''
    outmoney = money * exchange
    return outmoney

USD_VS_RMB = 6.67
#带单位的货币输入
currenct_str_value = input('请输入货币金额:  ')
unit = currenct_str_value[-3:]
if unit=='CHN':
    exchange_rate = 1/USD_VS_RMB

elif unit=='USD':
    exchange_rate = USD_VS_RMB
else:
    exchange_rate = -1

if exchange_rate != -1:
    in_str_monkey = currenct_str_value[:-3]
    in_monkey = eval(in_str_monkey)
    out_money = conver_currenct(in_monkey,exchange_rate)
    print('输出金额为 ： ',out_money)
else:
    print('不支持这种货币')



