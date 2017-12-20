'''
时间：2017、12，10
功能：
1.0 模拟掷骰子
2.0模拟投掷两个骰子
3.0散点图绘制，数据可视化
4.0对结果进行简单的数据分析

'''
import random
import matplotlib.pyplot as plt
#解决中文问题
plt.rcParams['font.sans-serif']=['SimHei']
#plt.rcParams['axes.unicode_miuns']=False
plt.rcParams['axes.unicode_minus'] = False

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

    total_times = 100
    rool_list = []

    for i in range(total_times):
       rool1 = roll_dice()
       rool2 = roll_dice()
       rool_list.append(rool1+rool2)

    #绘制直方图
    plt.hist(rool_list,bins=range(2,14),alpha = 0.5,edgecolor = 'black',linewidth = 1,normed=1)
    plt.title('骰子点数')
    plt.xlabel('点数')
    plt.ylabel('机率')
    plt.show()




if __name__ == '__main__':
    main()