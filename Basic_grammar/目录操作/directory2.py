import os, sys

path= '/tmp'
dirs = os.listdir(path)

print(dirs)

os.unlink(path+'/foo.txt')

print(os.listdir(os.getcwd()))