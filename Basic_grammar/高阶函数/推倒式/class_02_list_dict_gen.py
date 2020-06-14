"""
推到式

列表推到式

字典推到式

生成器表达式


"""

# 列表推到式
num = [i for i in range(10)]  # 列表推导式
print(num)
num = [i for i in range(0, 10, 2) if i % 2 == 0]  # 组合列表推导式和三目运算
print(num)
url = 'https://www.jianshu.com/page={}'
urls = [url.format(i) for i in range(10) if i != 0]
print(urls)

# 字典推到式

cook_str = 'BIDUPSID=D0727533D7147B7;PSTM=1530348042;BAIDUID=B1005C9BC2EB28;' \
           'sugstore=0;__cfduid=d0a13458f8ac2a;BD_UPN=12314353;ispeed_lsm=2;BDORZ=B490B5EBF6F3CD402'


def s_dir(cook_str):
    '''

    :param cook_str:  传入符合格式要求的字符串
    :return:
    '''
    return {i.split('=')[0]: i.split('=')[1] for i in cook_str.split(';')}


# 生成器表达式

tu = (i for i in range(5))  # 创建生成器表达式
print(next(tu))
print(next(tu))
print(next(tu))


# 生成器的三个方法

# send 和生成器内部进行数据交互
def func():
    i = 0
    while i < 10:
        print(f'函数{i}的数值')
        k = yield i
        if k is not None:
            i = k
        i += 1


res = func()
print(next(res))  # 在send前必须先next
print(res.send(4))  # 通过send控制生成器的值，动态修改
print(res.send(3))

res.close()  # 关闭生成器
print(next(res))  # 会报错因生成器已经关闭

print(res.throw(NameError, 'name is xxx'))  # 抛出指定错误
