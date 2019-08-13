def func2(func):
    def wrapper():
        print('运行装饰器')
        func()
    return wrapper
# res = func2()
# print(res())
@func2
def func():
    print('hans')

func()