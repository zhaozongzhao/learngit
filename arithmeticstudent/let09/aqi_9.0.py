'''
2.0json格式处理
3.0csv文件操作
4.0判断文件格式
5.0爬取天气情况
6.0 使用beautifulsoup 解析网页
7.0获取城市列表
'''

import pandas as pd

def main():
    '''
    主函数
    '''

    csv_df_obj = pd.read_csv('china_city_aqi3.csv')
    print(csv_df_obj)


    print('基本信息')
    print(csv_df_obj.info())


    print('最大值',csv_df_obj['AQI'].max())
    print('最小值', csv_df_obj['AQI'].min())
    print('平均值',csv_df_obj['AQI'].mean())

    #对数据进行排序
    csv_df_obj.sort_values(by=['AQI'])

    print('全国城市质量最好的5个城市 ： ')
    top_df_obj = csv_df_obj.sort_values(by=['AQI']).head(5)
    print(top_df_obj)

    print('全国城市质量最差的5个城市 ： ')
    top5_df_tail = csv_df_obj.sort_values(by=['AQI']).tail(5)
    print(top5_df_tail)

    print('全国城市质量最差的5个城市 ： ')
    top5_df_tail = csv_df_obj.sort_values(by=['AQI'],ascending=False).head(5)
    print(top5_df_tail)

    #保存csv
    top_df_obj.to_csv('top5_head.csv',index= False)
    top5_df_tail.to_csv('top5_df_tail.csv',index =False)

if __name__ == '__main__':
    main()