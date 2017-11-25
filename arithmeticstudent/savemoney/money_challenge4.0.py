'''
作者：赵宗召
时间 2017/11/12
功能52周存钱计划
增加功能：是用户能查询每周的存款金额
增加功能：判断日期是一年中的第几周

'''

import math
from datetime import datetime


def week_qure(input_str_date):
    '''
    根据用户输入时间判断，第几周
    '''
    now = datetime.strptime(input_str_date,format('%Y/%m/%d'))
    date = datetime.isocalendar(now)[1]
    return date

def money_inqure(list, week):
    '''
    根据周数，查询用户在该周的存款金额
    '''

    saving_week_money = list[week - 1]
    print(saving_week_money)


def count(money_per_week, total_week, increase_money):
    """
    根据用户指定的计划，计算账户金额
    """

    money_list = []  # 每周存款数的金额
    saved_miney_list = []  # 每周存款金额的列表
    # while i<=total_week:



    for i in range(total_week):
        # 更新账户余额
        money_list.append(money_per_week)

        saving = math.fsum(money_list)
        saved_miney_list.append(saving)
        # 更新每周存入金额
        money_per_week += increase_money

        # 输出
        print('存款金额{},这是您低{}周,下周存入{}'.format(saving, i + 1, money_per_week))
    return saved_miney_list


def main():
    '''
    主函数

    '''

    print('请输入您的计划（用空格隔开）')
    list_str = input('S首次存款金额 周数  递增金额')
    lists = list_str.split()
    money_per_week = eval(lists[0])
    total_week = eval(lists[1])
    increase_money = eval(lists[2])

    saving_list = count(money_per_week, total_week, increase_money)
    input_str_date = input('请输入您要日期 YYYY/NNNN/RRR')

    money_inqure(saving_list,int(week_qure(input_str_date)))


if __name__ == '__main__':
    main()
