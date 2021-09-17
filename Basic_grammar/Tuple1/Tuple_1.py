""""
时间：2021.09.17
功能： 元祖基础模块学习
人员：赵宗召
"""

#创建元祖

tup3 = ()
tup0 = (1,)  #元组中只包含一个元素时，需要在元素后面添加逗号来消除歧义
tup1 = (1,2,3,4)
tup2 = ('a','b','c','d')
tup4 = 'e','f'

print(tup3)
print(tup0)
print(tup1)
print(tup2)
print(tup4)

访问元祖
tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7);

#索引
print ("tup1[0]: ", tup1[0])
#切片
print ("tup2[1:5]: ", tup2[1:5])
print ("tup2[1:5:2]: ", tup2[1:5:2])
print ("tup2[::-1]: ", tup2[::-1])


#修改元祖
tup1 = ('physics', 'chemistry', 1997, 2000,[1,2,3])
tup2 = (1, 2, 3, 4, 5, 6, 7)

#合并元祖
print(tup1+tup2)
print(tup1*2)
tup1[4][0]=2
print(tup1)

