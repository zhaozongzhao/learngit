'''
时间：2017、12，10
功能：
1.0 模拟掷骰子
2.0模拟投掷两个骰子
3.0散点图绘制，数据可视化
4.0对结果进行简单的数据分析
5.0科学计算方法

'''
import random
import matplotlib.pyplot as plt
import numpy as np
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

    total_times = 10000
    #生成点数的随机数
    rool_list1 = np.random.randint(1,7,size=total_times)
    rool_list2 = np.random.randint(1,7,size=total_times)
    rool_list = rool_list1 + rool_list2

    print(rool_list1)
    print('******************************************')
    print(rool_list2)
    print('******************************************')
    print(rool_list1)

    #生成x轴的坐标点数
    tick_xlabel = ['2点','3点','4点','5点','6点',
                   '7点', '8点', '9点', '10点', '11点','12点']
    top_list = np.arange(2 , 13)+0.5
    #设置x轴显示
    plt.xticks(top_list,tick_xlabel)



    #绘制直方图
    plt.hist(rool_list,bins=range(2,14),alpha = 0.5,edgecolor = 'black',linewidth = 1,normed=1,rwidth=0.8)
    plt.title('骰子点数')
    plt.xlabel('点数')
    plt.ylabel('机率')
    plt.show()




if __name__ == '__main__':
    main()