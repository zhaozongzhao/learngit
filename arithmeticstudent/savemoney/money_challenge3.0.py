'''
作者：赵宗召
时间 2017/11/12
功能52周存钱计划
增加功能：是用户能查询每周的存款金额

'''

import  math

def money_inqure(list,week):
    saving_week_money=list[week-1]
    print(saving_week_money+10)


def count(money_per_week,total_week,increase_money):
    money_list = []
    # while i<=total_week:



    for i in range(total_week):
        # 更新账户余额
        money_list.append(money_per_week)
        saving = math.fsum(money_list)
        # 更新每周存入金额
        money_per_week += increase_money
        # 输出
        print('您当前存入金额{},这是您低{}周,存入{}'.format(saving, i + 1, money_per_week))
    return money_list



def main():
    '''
    主函数

    '''

    print('请输入您的计划（用空格隔开）')
    list_str = input('存款金额 周数  每周递增金额')
    lists = list_str.split( )
    money_per_week = eval(lists[0])
    total_week = eval(lists[1])
    increase_money = eval(lists[2])
    saving_list= count(money_per_week,total_week,increase_money)
    week_str = int(input('请输入您要查询的周数'))
    money_inqure(saving_list,week_str)



if __name__ == '__main__':
        main()