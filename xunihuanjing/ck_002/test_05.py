'''
魔术方法
'''

# class A:
#     def __init__(self,value):
#         self.value = value
#
#     def __call__(self, *args, **kwargs):
#         print('调用__call__')
#
# a = A('name')
# print(a.value)
# print(a)


dict1 = {1:2,2:1}
dict2 = {3:2,2:1}
for i ,v in dict1.items():
    try:
        dict2.pop(i)
    except Exception as E:
        print(E)
print(dict2)