from enum import Enum,unique
# month = Enum('Month',('jan','Feb','Mar','Apr'))
#
# for name,member in month.__members__.items():
#     print(name,'=>',member,',',member.value)
#
#
#
# @unique
# class Weekday(Enum):
#     sun = 0
#     mon = 1
#     tue = 2
#     web = 3
#     thu = 4
#
# day1 = Weekday.mon
# print(day1)
# print(Weekday.tue)
#

class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):


    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')