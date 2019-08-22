dict = {}
dict['one'] = '1-课程'
dict[2] = '2-课程'
tindict = {'name':'赵宗召','code':'1','site':'www.baidu.com'}
# print(dict['one'])
# print(dict[2])
# print(dict)
# print(tindict.keys())
# print(tindict.values())
print(tindict.pop('name'))
print(tindict)
#
list = ('1',2,3)
dict2 =dict.fromkeys(list,10)
print(dict2)
#
# print(dict2.get('name'))
#
# print(2 in dict2)
#
# print(dict2.items())
#
# print(dict2.update(dict))
# print(dict2)
#
print(dict2.pop(2))
#
# print(dict2.popitem())