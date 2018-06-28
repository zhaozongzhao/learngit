#能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径
import os
def get_walk(patah):
    list = []
    for i in os.walk(patah):
       list.append(i)
    return list



def get_file_path(zzz):
    path = os.getcwd()
    filename = get_walk(path)
    list = []
    for j in filename:
      for name in j[2]:
        if zzz in name:
            list.append(name)
    path1 = os.path.split(path)
    for i in list:
        path2 = os.path.join(path1[0],i)
        print(path2)



get_file_path('file')