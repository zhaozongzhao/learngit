'''
作者： 赵宗召
时间：2017/11/26
功能：输入某年某月某日，判断这是一年的第几天
新增功能：用列表来替换元祖
'''
from datetime import  datetime


def Leapyear(year):
    '''
    判断是否是闰年，如果是当时间大于2月。天数加一
    '''
    # 判断闰年
    is_lead_year = False
    if year % 400 == 0 or ((year % 4 == 0) and (year % 100 != 0)):
        is_lead_year = True
    return  is_lead_year

def date(input_str_date):
    inpur_date = datetime.strptime(input_str_date, format('%Y/%m/%d'))

    # 获取年月日
    year = inpur_date.year
    month = inpur_date.month
    day = inpur_date.day

    return year,month,day
def main():
    ''''
    主函数
    '''
    input_str_date = input('请输入某年某月某日  YY/MM/DD:')
    date1 = date(input_str_date)
    year = date1[0]
    month = date1[1]
    day = date1[2]
    #定义一个元祖用来存储，一年的月份的天数
    days_in_month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    #计算当前月份之前的天数和当前月份天数
    if Leapyear(year):
        days_in_month_list[1] = 29
    das = sum(days_in_month_list[:month-1])+day

    #判断闰年
    # if Leapyear(year) and  month > 2:
    #         das +=1

    print('这是{}年的第{}天 ： '.format(year,das))

if __name__ == '__main__':
    main()
