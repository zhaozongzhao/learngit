'''
2.0json格式处理
3.0csv文件操作
4.0判断文件格式
'''
import json
import os
import csv


def process_jaon_file(filepath):
    '''
    json文件解码
    '''
    # f = open(filepath,mode='r',encoding='utf-8')
    # city_list = json.load(f)
    # return  city_list
    with open(filepath,mode='r',encoding='utf-8') as f:
        city_list = json.load(f)
    print(city_list)

def process_csv_file(filepath):
    '''
    处理csv文件
    '''
    with open(filepath,mode='r',encoding='utf-8',newline= '') as f:
        reder = csv.reader(f)
        for i in  reder:
            print(','.join(i))





def main():
    '''
    主函数
    '''
    filepath = input('请输入文件路径： ')
    filename,filetxt = os.path.splitext(filepath)
    if filetxt == '.json':
        process_jaon_file(filepath)
        pass
    elif filetxt == '.csv':
        process_csv_file(filepath)
        pass
    else:
        print('不支持当前格式')


    # city_list = process_jaon_file(filepath)
    # city_list.sort(key=lambda city: city['aqi'])
    # top5_list = city_list
    # #json文件写入
    # f = open('top5.json',mode='w',encoding='utf-8')
    # json.dump(top5_list,f,ensure_ascii=False)
    # f.close()

    #print(city_list)
if __name__ == '__main__':
    main()