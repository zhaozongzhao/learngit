'''
读取文件数据
'''

#读取txt文件
def read_txt(filename):
    path = 'C://Users//zzz//learngit//xinyuezx//xinyuedata//data/'
    file = path + filename
    user_file = open(file,'r')
    lines = user_file.readlines()
    user_file.close()
    return  lines

#读取csv文件
import csv
from itertools import islice

def read_csv(filename):
    path = 'C://Users//zzz//learngit//xinyuezx//xinyuedata//data/'
    file = path + filename
    user_file = open(file,'r')
    date = csv.reader(user_file)
    list=[]#每一行已一个
    print(date)
    for i in date:
        list.append(i)
    return  list






def main():
    #j = read_txt('user_info.txt')
    list = read_csv('title.csv')
    title = []
    h = []
    for i in islice(list,1,None):
        title.append(i[0])
        h.append(i[1])
    print(title,h)





if __name__ == '__main__':
    main()
