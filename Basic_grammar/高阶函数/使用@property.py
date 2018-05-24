# class student(object):
#
#     def get_score(self):
#         return self._score
#
#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an intaeger')
#         if value < 0 or value >100:
#             raise ValueError('score must be an intaeger')
#         self._score = value
#
# s = student()
# s.set_score(60)
# print(s.get_score())
# s.set_score(9999)
# print(s.get_score())

class  Student(object):


    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
         if not isinstance(value,int):
             raise ValueError('score must be an intaeger')
         if value < 0 or value >100:
             raise ValueError('score must be an intaeger')
         self._score = value

s = Student()
s.score = 60
print(s.score)
s.score = 9999

