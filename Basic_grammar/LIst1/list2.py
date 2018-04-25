#列表函数

list1 = ['123','aabbcc',1234]
tupe = ('hahah',121314)

print(len(list1))

# print(max(list1))
#
#
# print(min(list1))
print(type(list(tupe)))


list1.append('hhhh')
print(list1)


print(list1.count('123'))

list1.extend(list(tupe))

print(list1)



print(list1.index(1234))

list1.insert(1,'xxx')
print(list1)

list1.pop()
print(list1)

list1.remove('123')
print(list1)


list1.reverse()
print(list1)

list2 = list1.copy()

print(list2)

list1.clear()

print(list1)