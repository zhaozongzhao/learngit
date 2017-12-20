'''
10.0使用pandas进行数据过滤，和数据可视化
'''

import pandas as pd
import matplotlib.pyplot as plt

#解决中文问题
plt.rcParams['font.sans-serif']=['SimHei']
#plt.rcParams['axes.unicode_miuns']=False
plt.rcParams['axes.unicode_minus'] = False
def main():
    '''
    主函数
    '''

    csv_df_obj = pd.read_csv('china_city_aqi3.csv')

    print('基本信息')
    print(csv_df_obj.info())

    print('数据清理')
    clear_aqi_dada = csv_df_obj[csv_df_obj['AQI'] > 0]


    print('最大值',clear_aqi_dada['AQI'].max())
    print('最小值', clear_aqi_dada['AQI'].min())
    print('平均值',clear_aqi_dada['AQI'].mean())

    #对数据进行排序
    clear_aqi_dada.sort_values(by=['AQI'])

    print('全国城市质量最好的5个城市 ： ')
    top_df_obj = clear_aqi_dada.sort_values(by=['AQI']).head(5)
    print(top_df_obj)

    print('全国城市质量最差的5个城市 ： ')
    top5_df_tail = clear_aqi_dada.sort_values(by=['AQI']).tail(5)
    print(top5_df_tail)

    print('全国城市质量最差的5个城市 ： ')
    top5_df_tail = clear_aqi_dada.sort_values(by=['AQI'],ascending=False).head(5)
    print(top5_df_tail)

    #保存csv
    top_df_obj.to_csv('top5_head.csv',index= False)
    top5_df_tail.to_csv('top5_df_tail.csv',index =False)

    #数据
    top50_df_obj = clear_aqi_dada.sort_values(by=['AQI']).head(50)
    top50_df_obj.plot(kind = 'bar',x = 'City',y = 'AQI',title = '环境最好的城市',figsize = (20,10))
    plt.xlabel('城市名称')
    plt.ylabel('aqi质量')
    plt.savefig('top50_city_aqi.png')
    plt.show()



if __name__ == '__main__':
    main()