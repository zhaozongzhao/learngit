# 日志打印装饰器


def logger(func):
    """

    :param func: 这是装饰器函数，参数 func 是被装饰的函数
    :return: 返回内部函数的函数名
    """

    def wrapper(*args, **kw):
        print('主人，我准备开始执行：{} 函数了:'.format(func.__name__))

        # 真正执行的是这行。
        func(*args, **kw)

        print('主人，我执行完啦。')

    return wrapper


@logger
def add(x, y):
    print('{} + {} = {}'.format(x, y, x + y))


add(1, 3)

# 时间计时器

import time


def timer(func):
    def wrapper(*args, **kw):
        t1 = time.time()
        # 这是函数真正执行的地方
        func(*args, **kw)
        t2 = time.time()

        # 计算下时长
        cost_time = t2 - t1
        print("花费时间：{}秒".format(cost_time))

    return wrapper


@timer
def add_time(x, y):
    print('{} + {} = {}'.format(x, y, x + y))


add_time(1, 3)


# 带参数的装饰器


def say_hello(contry):  # contry装饰器的参数
    def wrapper(func):  # 传入装饰器的类
        def deco(*args, **kwargs):
            if contry == "china":
                print("你好!")
            elif contry == "america":
                print('hello.')
            else:
                return

            # 真正执行函数的地方
            func(*args, **kwargs)

        return deco

    return wrapper


# 小明，中国人
@say_hello("china")
def xiaoming():
    pass


# jack，美国人
@say_hello("america")
def jack():
    pass


xiaoming()
jack()


# 不带参数的类装饰器

class logger(object):
    def __init__(self, func):  # 函数在初始化操作触发，通过此方法我们可以定义一个对象的初始操作
        self.func = func

    def __call__(self, *args, **kwargs):  # 创建类并返回这个类的实例
        print("[INFO]: the function {func}() is running..." \
              .format(func=self.func.__name__))
        return self.func(*args, **kwargs)


@logger
def say(something):
    print("say {}!".format(something))


say("hello")


# 带参数的类装饰器：

class logger1(object):
    def __init__(self, level='INFO'):  # 接收传入参数
        self.level = level

    def __call__(self, func):  # 接受函数
        def wrapper(*args, **kwargs):
            print("[{level}]: the function {func}() is running..." \
                  .format(level=self.level, func=func.__name__))
            func(*args, **kwargs)

        return wrapper  # 返回函数


@logger
@logger1(level='WARNING')
def say1(something):
    print("say {}!".format(something))


say1(123)

# 使用偏函数与类实现装饰器


import functools


class DelayFunc:
    def __init__(self, duration, func):
        self.duration = duration
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Wait for {} seconds...'.format(self.duration))
        time.sleep(self.duration)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        print('Call without delay')
        return self.func(*args, **kwargs)


def delay(duration):
    """
    装饰器：推迟某个函数的执行。
    同时提供 .eager_call 方法立即执行
    """
    # 此处为了避免定义额外函数，
    # 直接使用 functools.partial 帮助构造 DelayFunc 实例
    return functools.partial(DelayFunc, duration)


@delay(duration=4)
def add_delay(a, b):
    return a + b


print(add_delay(3, 4))

# 装饰类的装饰器

instances = {}

def singleton(cls):
    def get_instance(*args, **kw):
        cls_name = cls.__name__
        print('===== 1 ====')
        if not cls_name in instances:
            print('===== 2 ====')
            instance = cls(*args, **kw)
            instances[cls_name] = instance
        return instances[cls_name]
    return get_instance

@singleton
class User:
    _instance = None

    def __init__(self, name):
        print('===== 3 ====')
        self.name = name
        
User()