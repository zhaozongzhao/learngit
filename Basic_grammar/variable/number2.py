#随机数函数
import random
list = [1,2,3,4,5,6]
trup = (1,2,3,4,5)
str = 'helloword'

print(random.choice(list))   #随机获取列表,元祖,字符串中的数据
print(random.choice(trup))
print(random.choice(str))

#randrange函数

print(random.randrange(1,100,5))  #获取制定范围中的数据,设置部长

#random

print(random.random()) #随机获取[0,1)数据


#shuffle()将所有序列的元素随机排列
random.shuffle(list)
print(list)

#unifrom 在范围随机生成下一个实数
print(random.uniform(2,3))
