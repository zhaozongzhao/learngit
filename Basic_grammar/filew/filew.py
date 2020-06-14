f = open('/tmp/foo.txt', 'r')

# f.write('第二行\n第三行')
# str = f.read()
# print(str)


str1 = f.readline()
print(str1)

str2 = f.tell()
print(str2)

f.close()
