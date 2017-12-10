'''
2.0json格式处理
3.0csv文件操作
'''
import json

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
    city_list = process_jaon_file(filepath)
    city_list.sort(key=lambda city: city['aqi'])
    top5_list = city_list
    #json文件写入
    f = open('top5.json',mode='w',encoding='utf-8')
    json.dump(top5_list,f,ensure_ascii=False)
    f.close()

    #print(city_list)
if __name__ == '__main__':
    main()