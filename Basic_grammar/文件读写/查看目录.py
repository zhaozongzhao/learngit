import os
print(os.listdir())#查看当前文件所有目录
#os.path.isdir() #判断是否是目录

#判断是否为目录
for i in os.listdir():
   if os.path.isdir(i):
       print(i)


print([x for x in os.listdir('.') if os.path.isdir(x)])

#筛选出所有.py文件
for i in os.listdir():
    if os.path.isfile(i) and os.path.splitext(i)[1] == '.py':
        print(i)

