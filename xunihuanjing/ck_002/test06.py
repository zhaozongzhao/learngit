
"""
1、面向对象的三大特征是什么？多态又是什么？
   答： 封装：将数据与操作数据的源代码进行有机的结合，形成“类”，目的是增强安全性和简化编程
        继承: 继承就是子类继承父类的特征和行为,python中一个类可以继承多个类也可以继承一个，继承的类叫做子类，被继承的
        称为父类或者基类
        多态: 多态同一个行为具有多个不同表现形态的能力。是指一个类实例（对象）的相同方法在不同情形有不同表现形式
        多态存在的三个必要条件：
           继承
           重写（子类继承父类后对父类方法进行重新定义）
           父类引用指向子类对象
"""
"""
2、私有属性怎么定义，不同的定义方式有什么区别
   定义私有： 以单下划线和双下划线开头的属性称之为私有属性
   区别 : 以单下划线开头的表示的是protected类型的变量。即保护类型只能允许其本身与子类进行访问
          双下划线的表示的是私有类型的变量。只能允许这个类本身进行访问了

"""
"""
3、自定义一个类
    1、通过上课的相关知识点对类属性进行限制，只能设置三个属性  name    age   data
    2、通过相关机制对设置的属性类型进行限制，name只能设置字符串类型数据    age设置为int类型数据  data不做要求
    3、通过相关机制实现，name 属性不能进行删除
    4、当age 设置的值少于0时，确保查询出来的值为0，
"""

class Course(object):
    """
      第三题作业题
    """
    __slots__ = ['name','age','data']

    def __setattr__(self, key, value):
        if key == 'name':
            if isinstance(value,str):
                object.__setattr__(self,key,value)
        elif key == 'age':
            if isinstance(value, int):
                object.__setattr__(self, key, value)
        else:
            object.__setattr__(self,key,value)

    def __getattribute__(self, item):
        if item == 'age':
           if object.__getattribute__(self,item)<= 0:
               return 0
           else:
               return  object.__getattribute__(self,item)

        else:
            object.__delattr__(self, item)

    def __delattr__(self, item):
        if item == 'name':
            pass
        else:
            object.__delattr__(self,item)

c = Course()
c.age = 10
print(c.age)
# c.stature = 167



# print(Course.__dict__)
# print(Course.__doc__)
# # print(Course.func.__doc__)







