'''
作者：赵宗召
时间 2017/11/12
功能52周存钱计划

'''

import  math




def main():
    '''
    主函数

    '''
    print('请输入您的计划（用空格隔开）')
    list = input('每周存款金额 周数  每周递增金额')
    money_per_week = 10    #每周存入金额
    # i = 1                  #周数
    increase_money = 10    #递增的余额
    total_week=52          #总周数
    saving = 0             #账户余额

    money_list = []
    # while i<=total_week:
    for i in range(total_week):
        #更新账户余额
        money_list.append(money_per_week)
        saving =math.fsum(money_list)
        #更新每周存入金额
        money_per_week+=increase_money
        #输出
        print('您当前存入金额{},这是您低{}周,存入{}'.format(saving,i+1,money_per_week))



if __name__ == '__main__':
        main()