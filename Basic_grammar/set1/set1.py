student = {1,2,3,4,1,5}
print(student) #集合会自动去除重复的元素

#逻辑判断
if (1 in student):
    print('1 in ')
else:
    print('1 not')


#set可以进行集合

a =set('abcd')
b = set('eabfg')

print(a)
print(a-b)   #a 和 b 的差集
print(a|b)   #a 和 b 的并集
print(a&b)   #a 和 b 的交集
print(a^b)   #a 和 b 中不同时存在的元素

