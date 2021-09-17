# h = list(range(1,11))
# print(h)
#
# #列表生成
# a = [i*4 for i in range(1,11)]
# print(a)

num = [i for i in range(100)] #列表推导式
print(num)
num = [i for i in range(0,100,2) if i % 2 == 0]  #组合列表推导式和三目运算
print(num)

# b = [x*x for x in range(1,11) if x %2 ==0]
# print(b)


#嵌套列表解析
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# w = []
# for a in range(3):
#     h = []
#     for i in matrix:
#          h.append(i[a])
#     w.append(h)
#
# print(w)
#
#
#
# for a in range(3):
#     h = []
#     for i in matrix:
#         for int1 in range(3):
#              h.append(i[int1])
# str =str(h)
#
# print(str)
