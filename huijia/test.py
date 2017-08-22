'''amount=0
amount='显示第 1 到第 10 条记录，总共 4647 条记录'
substr='共'
print(amount)
print(amount.rfind(substr))
h=amount[18:-3]
print(h)
w=h.strip().lstrip().rstrip(' ')
j=float(w)
if j>100:
    print('正确')
else:
    print('错误')'''

class count:
    def __init__(self,a,b):
        self.a=int(a)
        self.b=int(b)
    def add(self):
        return self.a+self.b
