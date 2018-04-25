# import os, sys
#
# path= '/tmp'
# dirs = os.listdir(path)
#
# print(dirs)
#
# os.makedirs(path+'/test')
#
# dirs = os.listdir(path)
#
# print(dirs)
#

import os



#打开文件
fd  = os.open('/tmp/foo.txt',os.O_RDWR)


#读取文件
ret = os.read(fd,12)
print(ret)


#关闭文件
os.close(fd)

