# 将用户输入的所有数字（正数、浮点数，不包括0和非数字类型的字符串）相乘之后对23取余数
# a.用户输入的数字个数不确定（使用input提示用户输入，任意输入数字），输入的每个数字之间以#号分割，标准格式例如："10#12#-3#11.2#9" （5分）
# b.如果用户输入的数字前后有空格，也能正常计算，例如：" 10# 12 #-3 #11.2 # 9 " （5分）
# c.用户输入的无效数字需要打印出来，无效数字例如：”1a"、”lemon“、”@“、”12.2.1“、”11..2“等 （8分）
# d.要求将用户计算的结果保存到文件，下次执行程序之前，显示历史记录。 （7分）
# 例如：
# 第一次计算的值为2
# 第二次计算的值为1
# from functools import reduce
# i= 'Y'
# h = 1
# filename =  open('/Users/hnbl009/gitfile/learngit/面试题验证/1.txt','r+')
# filenamezz = filename.read()
# print(filenamezz)
# while i=='Y' or i=='y':
#
#   x = input('请输入参数以#隔开')
#   filename.write('输入参数为{}\n'.format(x))
#   p =  x.split('#')
#   if len(p) >1:
#      s =[]
#      for i in p :
#          try:
#            i = float(i)
#            s.append(i)
#          except Exception as e:
#            print('无效参数{}'.format(i))
#            filename.write('无效参数{}\n'.format(i))
#      r = reduce(lambda x,y: x*y,s)%23
#      print('第{}次计算的值为{}'.format(h,r))
#   elif len(p) == 1 and int(p[0])!= 0:
#      print('第{}次计算的值为{}'.format(h,float(p[0])%23))
#      filename.write('第{}次计算的值为{}\n'.format(h,p[0]))
#   else:
#       print('输入的数字无效{}'.format(p))
#
#
#
#   h+=1
#   i= input('是否退出,继续Y 退出N')
#
# filename.close()

# 面试题2:
# 创建一个老板类Boss：
# •	拥有金钱、商品 、员工列表 3 个属性，（4分）
# •	一个雇佣员工的方法（把员工添加到员工列表中）;（2分）
# •	卖产品的方法（卖一个商品品能够获得金钱10），（2分）
#
# 创建一个员工类Employee：
# •	拥有 熟练度 属性(熟练度每年增加50) （2分）
# •	有一个工作的方法（每个员工每个月生产商品的数量等于员工的技能熟练度，并且需要 boss 支付2000元工资）（5分）
# 老板的初始化金钱为10000,产品为0，第一年只雇佣一个员工，以后每年会增加一个员工（员工初始化熟练度为300，熟练度最高可以达到500），定义一个函数，计算10年后老板的金钱为多少？(10分)

class Boss():

    def __init__(self,money,goods,list3):
        self.money = money
        self.goods = goods
        self.list3 = list3

    def employees(self,emplyess):
         self.list3.append(emplyess)
         return self.list3

    def sell(self,num):
      self.good =self.goods-num

      self.money = num * 10
      return self.money



class Employee(Boss):

    def __init__(self,proficiency,attribute=300):
        self.attribute = attribute
        self.proficiency = proficiency


    def yearattribute(self):
        if self.attribute >500:
           return  self.attribute+50
        else:
           return  self.attribute

    def yearwork(self,goods,moneys):

        self.attribute = self.attribute + goods
        moneys  = moneys-2000

        return self.attribute,moneys






list=[]
Boss =Boss(0,100,list)
print(Boss.employees('张三'))
print(Boss.sell(5))


