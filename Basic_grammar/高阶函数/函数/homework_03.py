"""
1、古典问题：有一对小兔子，第三个月起每个月都生一对兔子，每对小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问n个月的后的兔子总
数为多少？（意味着兔子生长期为2个月，第三个月开始生小兔组）  使用递归实现？


"""
from functools import lru_cache


@lru_cache(maxsize=128)
def fun1(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fun1(n - 1) + fun1(n - 2)


print(fun1(9))

"""
2、小明有100元钱 打算买100本书，A类书籍5元一本，B类书籍3元一本，C类书籍1元两本，请用程序算出小明一共有多少种买法?（面试笔试题）

"""


def Buy_book(money, book):
    num = 0
    for a in range(int(money / 5)):
        for b in range(int(money / 3)):
            for c in range(int(book + 1)):
                if a * 5 + b * 3 + c * 0.5 <= book and a + b + c == book:
                    print('5元书买{}本，3元书买{}本，1元书买{}本'.format(a, b, c))
                    num += 1
    return num


num = Buy_book(100, 100)
print('第二题，总共{}方法'.format(num))


# 方法二


def buy_book2():
    count = 0
    for a in range(21):
        for b in range(34):
            c = 100 - a - b
            if a * 5 + b * 3 + c * 0.5 <= 100:
                count += 1
    return count


num = buy_book2()
print('第二题，总共{}方法'.format(num))

"""
3、现在有一个列表   li = [11,21,4,55,6,67,123,54,66,9,90,56,34,22], 请将 大于5的数据过滤出来，然后除以2取余数，

"""
li = [11, 21, 4, 55, 6, 67, 123, 54, 66, 9, 90, 56, 34, 22]
print(list(map((lambda x: x % 2), list(filter((lambda x: x > 5), li)))))

"""
4、有一个列表 li2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],请用上课讲的知识处理成下面的格式：

   li4 = [[1,2,3],[4,5,6],[7,8,9][10,11,12],[13,14,15]]
"""
li2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


# 方法1
def fun4(li2):
    li4 = iter(li2)
    li3 = list(zip(li4, li4, li4))
    h = 0
    for i in li3:
        li3[h] = list(i)
        h += 1
    print(li3)


fun4(li2)


# 方法2
def fun5(li2):
    zip_object = zip(li2[::3],li2[1::3],li2[2::3])
    res = map(lambda x:list(x),zip_object)
    print('第四题答案结果为：{}'.format(list(res)))


fun5(li2)