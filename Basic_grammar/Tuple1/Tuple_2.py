""""
时间：2021.09.17
功能： 命名元祖学习
人员：赵宗召
"""



from collections import namedtuple
#定义一个类
Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
#创建对象
s = Student('Jim', 21, 'male', '123@qq.com')
# 3、获取命名元组的值
print(s.name)   #支持元祖的索引取值
print(s[0])     #支持切片
print(s[::-1])  #支持通过字段名来取值