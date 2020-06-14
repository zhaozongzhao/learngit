# 类定义
class pepple:
    """

    """
    # 定义基本属性
    name = ''
    age = 0

    # 定义私有属性
    __weught = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        """
        整体描述模块作用
        :param n:  参数 ： 作用
        :type  n:  参数 ： 参数类型

        """
        self.name = n
        self.age = a
        self.__weught = w

    def speak(self):
        print('{}说: 我{}岁了'.format(self.name, self.age))


p = pepple('ken', 10, 163)

print(p.speak())


# 单继承实例:
class student(pepple):
    grade = ''

    def __init__(self, n, a, w, g):
        pepple.__init__(self, n, a, w)
        self.grade = g

    # 覆盖父类的方法
    def speak(self):
        print('{}说: 我{}岁了,我在读{}年级'.format(self.name, self.age, self.grade))


s = student('ken1', 5, 2, 3)
print(s.speak())


# 另一个类,多继承之前的准备

class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample('Time', 25, 80, 4, 'python')

test.speak()
