'''
时间：2017、12，10
功能：
1.0 模拟掷骰子

'''
import random
def roll_dict():
  '''
  模拟掷骰子
  '''
  rool = random.randint(1,6)
  return rool

def main():
    '''
    主函数
    '''

    total_times = 5
    #初始化列表[0，0，0，0，0，0]
    result_list = [0]*6

    for i in range(total_times):
       rool = roll_dict()
       for j in range(1,7):
           if j == rool:
               result_list[j-1]+=1
    print(result_list)
    for i,y in enumerate(result_list):
        print('点数{}的次数{}，频率{}'.format(i+1,y,y/total_times))




if __name__ == '__main__':
    main()