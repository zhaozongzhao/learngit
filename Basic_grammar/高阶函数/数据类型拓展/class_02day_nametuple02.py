# ： 数值类型

int(123444)  # 整型
float(1.234)  # 浮点型
bool(False or True)  # 布尔型
# complex(5i + 1)  # 复数



#  序列类型 、

#列表
a = [1, 2, 3, 4] # 列表(list) 》》可变，可迭代
# 增
a = []
b = 'b' #元素
c = [1, 2, 3] #可迭代对象
#增加单个元素
a.append(b)
print(a)
['b']
#增加序列对象
a.extend(c)
print(a)
['b', 1, 2, 3]
#索引增加
a.insert(2, b)
print(a)
['b', 1, 'b', 2, 3]

#删除
a = [1, 2, 3, 'a', 'b', 'c']
#按照索引删除单个元素，默认索引值为-1（最右）
a.pop(1)
print(a)
[1, 3, 'a', 'b', 'c']
#删除指定元素
a.remove('a')
print(a)
[1, 3, 'b', 'c']
#索引删除(python自带)
del a[0]
print(a)
a = [3, 'b', 'c']

#改
a = [1, 2, 3, 4, 5, 6]
#索引改
a[0] = 4
print(a)
[4, 2, 3, 4, 5, 6]
#排序（正序）
a.sort()
print(a)
[2, 3, 4, 4, 5, 6]
#逆序
a.reverse()
print(a)
[6, 5, 4, 4, 3, 2]
#复制（地址变化）
b = a.copy()
print(b)
[6, 5, 4, 4, 3, 2]

# 查
a = [4, 2, 3, 4, 5, 6]
#查询索引
b = a.index(5)
print(b)
4
#查询出现次数
c = a.count(4)
print(c)
2

"""
元祖 (tuple)
由于元祖为不可变对象，因此其没有增删改方法，只能进行查询，查询方式参照列表。
如若需要对元祖内元素进行操作可以将元祖变成列表后处理。
"""
a = (1, 2, 3, 'a', 'b', 'c') #元祖(tuple) 》》不可变，可迭代
b = tuple(a)
print(b)
[1, 2, 3, 'a', 'b', 'c']

"""
字符串 'str'
"""

# 增
a = 'abc'
b = 'cde'
#拼接
c = a + b
print(c)
'abcdef'

# 删除
a = 'abcabc'
#将字符串中的'b'替换为'a'
a.replace('a', 'b')

# 改
a = 'abcdef'
#修改命令（返回字符串）
a.upper() #改为大写
a.lower() #改为小写
a.strip() #去(左右)空格
a.capitalize() #句子首字母大写
a.title() #单词首字母大写
a.split(a) #根据a将字符串切割

#查
a.isdigit() #是否数字
a.isalpha() #是否字母
a.endswith('a') #是否结尾
a.startswith('b') #是否开头
a.islower() #是否小写
a.isupper() #是否大写


"""
散列
"""

"""
集合 {set}
集合为无序不可重复对象，因此可用于去重操作
"""

a.add() #增加元素
a.update([a]) #增加序列，需要序列可迭代

a.pop() #随机删除
a.remove(a) #指定删除a元素

a.isdisjoin(b) #是否无交集
a.issubset(b) #a是否被b包含
a.issuperset(b) #a是否包含b

"""
字典 dict {'key': 'value'}
字典为无序对象，其键值不可重复
"""

#键值对增加
a(key) = value
dict(key = 'value')
a.setdefault('key', value) #有则改，无则增

#随机或指定删除
a.pop()
a.pop(key) #根据键值删除键值对
#清空
a.clear()
# 改
a.update(key, 'value') #按照键值修改value
# 查
a.get(key) #查找键值对应的value,不存在返回None
a.keys() #返回全部key
a.values() #返回全部value
a.items() #返回全部键值对,以列表形式返回。
