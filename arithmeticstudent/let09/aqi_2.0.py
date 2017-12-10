'''
2.0json格式处理
'''
import json
import csv

def process_jaon_file(filepath):
    '''
    json文件解码
    '''
    f = open(filepath,mode='r',encoding='utf-8')
    city_list = json.load(f)
    return  city_list

def main():
    '''
    主函数
    '''
    filepath = input('请输入文件路径： ')
    #对json文件解码操作
    city_list = process_jaon_file(filepath)
    city_list.sort(key=lambda city: city['aqi'])
    print(type(city_list))
    top5_list = city_list[:5]
    print(type(top5_list))
    lines = []
    #列名
    lines.append(list(top5_list[0].keys()))
    for city in top5_list:
        lines.append(list(city.values()))
    f = open('top.csv',mode='w',encoding='utf-8')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()




    #print(city_list)
if __name__ == '__main__':
    main()