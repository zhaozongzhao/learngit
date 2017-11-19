''''
   作者：赵宗召
   功能：绘制五角星
   版本：v1.1
   时间：2017.11.18
   功能：turtle库常用函数
   V1.1 新增功能：使用循环画五角星
   v1.2 将画五角星封装成函数
'''
import turtle
#画五角星
def pentagram(count,distance):
    while count <= 5:
        turtle.forward(distance)
        turtle.right(144)
        count = count + 1

def main():
    """
    主函数
    """

    distance=50
    while distance<=100:
        pentagram(1,distance)
        distance = distance + 10
        count = 1
        print(distance,count)
    turtle.exitonclick()
if __name__ == '__main__':
     main()