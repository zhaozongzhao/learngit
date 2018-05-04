#记录输入两个数之和
import cmath

class us():


    #计算输入两个数之和
    def us2(self,x,y):
        return float(x)+float(y)

    #计算一元二次方程
    def us3(self,a,b,c):
          d = (b**2)-4*a*b
          if d>=0:
               x1 = (-b-d/(2*a))
               x2 = (-b+d/(2*a))
               return x1,x2

          else:
              print('没有根')

u = us()
list = []
list.append(input('请输入x'))
list.append(input('请输入'))
list.append(input('请输入'))

print(u.us3(float(list[0]),float(list[1]),float(list[2])))




