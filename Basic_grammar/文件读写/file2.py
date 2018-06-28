#写入文件

path = '/Users/hnbl009/zzz.txt'
with open(path,'a') as f:
    f.write('hello word\n')
f = open(path,'r')
print(f.read())

