class Student():
    __slots__ = ('name','age')  #用tuple定义允许绑定的属性名称


s = Student()
s.name = 'zzz'
s.age = '13'
s.s='111'