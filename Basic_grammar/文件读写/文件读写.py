#/Users/hnbl009

path = '/Users/hnbl009/zzz.txt'

#方法一
try:
  #读取文件
  f = open(path,'r')
  print(f.read()) #读取文件
finally:
  if f:
     f.close()

#方法二
with open(path,'r') as f:
    print(f.read())


#方法三
f = open(path,'r')
for line in f.readline():
    print(line.strip())

path1 = '/Users/hnbl009/Desktop/测试图片/3.jpg'

f = open(path1,'rb')
print(f.read())