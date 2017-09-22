
import os


def find_file():
    #定义文件目录
    result_dir = 'C:\\report'



    #os.listdir 获取目录下所有文件及文件夹
    list = os.listdir(result_dir)

    list.sort(key=lambda fn: os.path.getatime(result_dir+'\\'+fn))

    print(('最新文件为：'+list[-1]))

    file=os.path.join(result_dir ,list[-1])

    return file ,list[-1]

