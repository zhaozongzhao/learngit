# 列表参数

import copy

list1 = [1, 'name', "password", [4, 5], (6, 7), {"name": 'pass'}]

#赋值
list2 = list1
#浅拷贝
list3 = list1.copy()
#深拷贝
list4 = copy.deepcopy(list1)

list1.append(10)
list1[3].append(6)

print(list1)
print(list2)
print(list3)
print(list4)

# #插入列表的指定位置
# list1.insert(0,0)
# print(list1)

# list_pop=list1.pop(1)
# print ("删除的项为 :", list_pop)
# print ("列表现在为 : ", list1)


# # 从指定位置开始搜索
# print ('name 索引值为', list1.index('name'))

# list1.append(7)
#
# print(list1.count(1))
#
# list2 = list(range(5))
# # 元组
# list_tuple = ('Spanish', 'Portuguese')
# # 集合
# list_set = {'Chinese', 'Japanese'}
# #添加列表
# list1.extend(list2)
# print('新列表: ', list1)
# # 添加元组元素到列表末尾
# list1.extend(list_tuple )
# print('新列表: ', list1)
#
# # 添加集合元素到列表末尾
# list1.extend(list_set)
# print('新列表: ', list1)
