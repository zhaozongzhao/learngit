'''
作者： 赵宗召
时间：2017/11/26
功能：输入某年某月某日，判断这是一年的第几天
'''
from datetime import  datetime

def main():
    ''''
    主函数
    '''
    input_str_date = input('请输入某年某月某日  YY/MM/DD:')
    inpur_date = datetime.strptime(input_str_date,format('%Y/%m/%d'))

    #获取年月日Sublime Text)
    year = inpur_date.year
    month = inpur_date.month
    day  = inpur_date.day

    #定义一个元祖用来存储，一年的月份的天数format
    days_in_month_tup = (31,28,31,30,31,30,31,31,30,31,30,31)
    #计算当前月份之前的天数和当前月份天数)
    das = sum(days_in_month_tup[:month-1])+day

    #判断闰年
    if year%400==0 or ((year%4==0)and (year%100!=0)):
        if month >2:
          das+=1

    print('这是一年的第{}天 ： '.format(das))

if __name__ == '__main__':
    main()
