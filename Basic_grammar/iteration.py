
#迭代器
# list = [1,2,3,4]
# list1 = iter(list)
# # for i in list1:
# #     print(i)
#
# print(next(list1))
# print(next(list1))
# print(next(list1))
# print(next(list1))


#列表生成器:

L1 = ['hello','world',18,'apple',None]
l2 = [ i for i in L1 if isinstance(i,str)]
print(l2)


