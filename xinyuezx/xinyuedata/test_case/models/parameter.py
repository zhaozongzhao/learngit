'''
读取文件数据
'''
import csv

from itertools import islice
#读取txt文件
def read_txt(filename):
    path = 'C://Users//zzz//learngit//xinyuezx//xinyuedata//data/'
    file = path + filename
    user_file = open(file,'r')
    lines = user_file.readlines()
    user_file.close()
    return  lines

#读取csv文件


def read_csv(filename):
    path = 'C://Users//zzz//learngit//xinyuezx//xinyuedata//data/'
    file = path + filename
   # with open(file,mode='r') as somfile:
    dats = csv.reader(open(file,mode='r'))
    return dats








def main():
    #j = read_txt('user_info.txt')
    list = read_csv('title.csv')
    for i in islice(list,1,None):
        print(i[0])
        print(i[1])






if __name__ == '__main__':
    main()
