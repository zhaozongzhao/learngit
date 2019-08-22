# def func2(func):
#     def wrapper():
#         print('运行装饰器')
#         func()
#     return wrapper
# # res = func2()
# # print(res())
# @func2
# def func():
#     print('hans')
#
# func()

def say_hello(contry):  #contry装饰器的参数
    def wrapper(func):  #传入装饰器的类
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


class logger(object):
    def __init__(self, func): #函数在初始化操作触发，通过此方法我们可以定义一个对象的初始操作
        self.func = func

    def __call__(self, *args, **kwargs): #创建类并返回这个类的实例
        print("[INFO]: the function {func}() is running..."\
            .format(func=self.func.__name__))
        return self.func(*args, **kwargs)

class logger1(object):
    def __init__(self, level='INFO'): #接收传入参数
        self.level = level

    def __call__(self, func): # 接受函数
        def wrapper(*args, **kwargs):
            print("[{level}]: the function {func}() is running..."\
                .format(level=self.level, func=func.__name__))
            func(*args, **kwargs)
        return wrapper  #返回函数
@logger
@logger1(level='WARNING')
def say1(something):
    print("say {}!".format(something))


#使用偏函数实现装饰器:
import time
import functools

class DelayFunc:
    def __init__(self,  duration, func):
        self.duration = duration
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Wait for {self.duration} seconds...')
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

@delay(duration=2)
def add(a, b):
    return a+b



if __name__ == '__main__':
    xiaoming()
    jack()
   #类装饰器
    say1("hello")
    print(add)
    print(add(1,1))