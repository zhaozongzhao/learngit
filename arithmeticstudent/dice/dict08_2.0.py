'''
时间：2017、12，10
功能：
1.0 模拟掷骰子
2.0模拟投掷两个骰子

'''
import random
def roll_dice():
  '''
  模拟掷骰子
  '''
  rool = random.randint(1,6)
  return rool

def main():
    '''
    主函数
    '''

    total_times = 10000
    #初始化列表[0，0，0，0，0，0]
    result_list = [0] * 11

    #初始话点数列表
    roll_list = list(range(2,13))
    roll_dict = dict(zip(roll_list,result_list))

    for i in range(total_times):
       rool1 = roll_dice()
       rool2 = roll_dice()

       for j in range(2, 13):
           if (rool1 + rool2) == j:
               roll_dict[j] += 1
    for i,y in roll_dict.items():
        print('点数{}的次数{}，频率{}'.format(i,y,y/total_times))




if __name__ == '__main__':
    main()