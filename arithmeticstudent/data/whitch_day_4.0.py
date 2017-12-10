'''
作者： 赵宗召
时间：2017/11/26
功能：输入某年某月某日，判断这是一年的第几天
新增功能：用字典储存数据
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

def date():
    try :
        input_str_date = input('请输入某年某月某日  YY/MM/DD:')
        inpur_date = datetime.strptime(input_str_date, format('%Y/%m/%d'))

        # 获取年月日
        year = inpur_date.year
        month = inpur_date.month
        day = inpur_date.day

        return year,month,day
    except Exception as  a:
        print('输入错误')
def main():
    ''''
    主函数
    '''

    date1 = date()
    year = date1[0]
    month = date1[1]
    day = date1[2]
    #定义一个
    month_day_dict = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

    for i in  range(1,month):
        day += month_day_dict[i]
    if Leapyear(year):
        day+=1


    print('这是{}年的第{}天 ： '.format(year,day))

if __name__ == '__main__':
    main()
