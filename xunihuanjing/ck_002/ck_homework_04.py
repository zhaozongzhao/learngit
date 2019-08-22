"""

第一题 ： 通过装饰器实现单例模式，只要任意一个类使用该装饰器装饰，那么就会变成一个单例模式的类。


第二题：自定义一个字典类型，实现对象可以之间可以 使用 + 和  -    来进行处理


第三题： 请描述 __new__ 、 __str__、__repr__、__call__分别在什么情况下会被触发！

"""
# 第一题
istest = {}


def B(func):
    def wrapper(*args, **kwargs):
        if not len(istest):  # 判断是否被实例化
            istest['ty'] = func(*args, **kwargs)
            return istest['ty']
        else:
            return istest['ty']

    return wrapper


@B
class A(object):
    def __init__(self, name):
        self.name = name


# 第二题

class dictadd(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{}'.format(self.value)

    def __add__(self, other):  # 相加操作
        for i, v in other.value.items():  # 循环遍历字典,将h2中的值加到h1中
            self.value[i] = v
        return dictadd(self.value)

    def __sub__(self, other):
        #方法1
        for i, v in other.value.items():
            try:
                self.value.pop(i)
            except Exception as e:
              pass

        return dictadd(self.value)
        # #方法2
        # return dictadd(dict(self.value.items() - other.value.items()) )
        #

# 第三题:
# __new__ :创建类并返回这个类的实例,创建类的时候出发
# __str__ :只要自己定义了__str__(self)方法,调用print输出时触发,__str__方法需要返回一个字符串
# __repr__:在没有__str__ 时使用print输出时触发,调用iter()时触发
# __call__:在只要定义类型的时候，实现__call__函数，这个类型就成为可调用的,在使用()调用时触发

if __name__ == '__main__':
    a = A('12345')
    print(id(a))
    b = A('12345678')
    print(id(b))

    # 字典相加
    c1 = {'b': '验证1'}
    c2 = {'c': 111, 'b': '验证2'}
    c3 = {'e': 111, 'f': '验证3'}
    d = dictadd(c1)
    c = dictadd(c2)
    e = dictadd(c3)
    print(d + c + e)

    # 字典相减
    h1 = {'name': 'xiaoming'}
    h2 = {'name': 'xiaoming', 'code': '1', 'site': 'www.baidu.com'}
    h3 = {1: 2, 2: 1, 'site': 'www.baidu.com'}
    h1 = dictadd(h1)
    h2 = dictadd(h2)
    h3 = dictadd(h3)
    print(h2 - h1 - h3)
