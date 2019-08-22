#
# 1、古典问题：有一对小兔子，第三个月起每个月都生一对兔子，每对小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问n个月的后的兔子总数为多少？（意味着兔子生长期为2个月，第三个月开始生小兔组）  使用递归实现？
# 2、小明有100元钱 打算买100本书，A类书籍5元一本，B类书籍3元一本，C类书籍1元两本，请用程序算出小明一共有多少种买法?（面试笔试题）
# 3、现在有一个列表   li = [11,21,4,55,6,67,123,54,66,9,90,56,34,22], 请将 大于5的数据过滤出来，然后除以2取余数，
# 4、有一个列表 li2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],请用上课讲的知识处理成下面的格式：
#  li4 = [[1,2,3],[4,5,6],[7,8,9][10,11,12],[13,14,15]]

# 第一题
def rabbit_number(month):
    if month == 1:
        return 1
    elif month == 2:
        return 1
    elif month == 3:
        return 2
    else:
        return rabbit_number(month - 1) + rabbit_number(month - 2)


# 第二题：
def Buy_book(money, book):
    num = 0
    for a in range(int(money / 5)):
        for b in range(int(money / 3)):
            for c in range(int(book + 1)):
                if a * 5 + b * 3 + c * 0.5 <= book and a + b + c == book:
                    print('5元书买{}本，3元书买{}本，1元书买{}本'.format(a, b, c))
                    num += 1
    return num


# 第三题：
def judge(n):
    return n > 5

def judge2(n):
    return n % 2

def judge3(li):
    return map(judge2, list(filter(judge, li)))

#第四题：
def conversion(li2):
    li4 = iter(li2)
    li3 = list(zip(li4, li4, li4))
    h = 0
    for i in li3:
        li3[h] = list(i)
        h+=1
    print(li3)


a = [1,2,3]
b = ['a', 'b', 'c']
print(list(zip(b, a)))





# if __name__ == '__main__':
#     li = [11, 21, 4, 55, 6, 67, 123, 54, 66, 9, 90, 56, 34, 22]
#     li2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#     print('兔子总数为{}对'.format (rabbit_number(20)))
#     print('100元钱 买100本书 共有{}中方法'.format(Buy_book(100,100)))
#     print(list(judge3(li)))
#     conversion(li2)
