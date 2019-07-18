# 将用户输入的所有数字（正数、浮点数，不包括0和非数字类型的字符串）相乘之后对23取余数
# a.用户输入的数字个数不确定（使用input提示用户输入，任意输入数字），输入的每个数字之间以#号分割，标准格式例如："10#12#-3#11.2#9" （5分）
# b.如果用户输入的数字前后有空格，也能正常计算，例如：" 10# 12 #-3 #11.2 # 9 " （5分）
# c.用户输入的无效数字需要打印出来，无效数字例如：”1a"、”lemon“、”@“、”12.2.1“、”11..2“等 （8分）
# d.要求将用户计算的结果保存到文件，下次执行程序之前，显示历史记录。 （7分）
# 例如：
# 第一次计算的值为2
# 第二次计算的值为1
from functools import reduce
i= 'Y'
h = 1
filename =  open('/Users/hnbl009/gitfile/learngit/面试题验证/1.txt','r+')
filenamezz = filename.read()
print(filenamezz)
while i=='Y' or i=='y':

  x = input('请输入参数以#隔开')
  filename.write('输入参数为{}\n'.format(x))
  p =  x.split('#')
  if len(p) >1:
     s =[]
     for i in p :
         try:
           i = float(i)
           s.append(i)
         except Exception as e:
           print('无效参数{}'.format(i))
           filename.write('无效参数{}\n'.format(i))
     r = reduce(lambda x,y: x*y,s)%23
     print('第{}次计算的值为{}'.format(h,r))
  elif len(p) == 1 and int(p[0])!= 0:
     print('第{}次计算的值为{}'.format(h,float(p[0])%23))
     filename.write('第{}次计算的值为{}\n'.format(h,p[0]))
  else:
      print('输入的数字无效{}'.format(p))



  h+=1
  i= input('是否退出,继续Y 退出N')

filename.close()