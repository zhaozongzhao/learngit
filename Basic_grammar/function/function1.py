#函数传入不可变实例

def ChangeInt(a):
    a = 10

b = 2
ChangeInt(b)
print(b)

#传入可变对象:

def changeme(list):
    list.append([1,2,3,4])
    print('函数内取值',list)
    return

list = [10,20,30]
changeme(list)
print('函数外取值',list)


#参数传递
#必须传递的参数
def printme(str):
    print(str)

printme(1)

#关键字参数:
def printme1(str):
    printme(str)

printme1(str= '关键字参数')


#默认参数
def printfo(name,age = 28):
    print(name,age)
    return

printfo('zzz')


#不定长参数
def printinfo(arg1,*var):
    print(arg1)
    for i in var:
        print(i )
    return


printinfo(1,2,3,4)


#匿名函数
sum = lambda s,y : s+y;
print(sum(1,2))
