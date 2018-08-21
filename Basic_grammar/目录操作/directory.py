#os 文件/目录操作的方法

#os.access(path,mode) path 检查是否有访问权限   mode权限
import os

ret = os.access('/tmp/foo.txt',os.F_OK) #判断路径是否存在

print(ret)
ret =os.access('/tmp/foo.txt',os.R_OK)    #判断是否有读取权限

print(ret)

ret = os.access('/tmp/foo.txt',os.W_OK)  #判断是否有写入权限

print(ret)


ret = os.access('/tmp/foo.txt',os.X_OK)    #判断是否可执行

print(ret)


#os.chdir(path) 切换路径

import os

path = '/tmp'

retval = os.getcwd() #查看当前工作目录
print(retval)

os.chdir(path)       #修改工作目录
retval = os.getcwd() #查看修改后的工作目录

print(retval)

print('当前目录:{}'.format(os.getcwd()))

# /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6