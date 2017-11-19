''''
   作者：赵宗召
   功能：绘制五角星
   版本：v2.0
   时间：2017.11.18
   功能：turtle库常用函数
   V1.1 新增功能：使用循环画五角星
   v1.2 将画五角星封装成函数
   V2.0 设置画笔的颜色和宽度
   V2.0 设置画笔的颜色和宽度
'''
import turtle
#画五角星
def pentagram(count,distance):
    count = 1
    while count <= 5:
        turtle.forward(distance)
        turtle.right(144)
        count = count + 1

def main():
    """
    主函数
    """
    #抬起画笔
    turtle.penup()
    turtle.backward(20)
    #放下画笔
    turtle.pendown()
    #画笔宽度
    turtle.pensize(2)
    #设置画笔颜色
    turtle.pencolor('red')

    distance=50
    while distance<=100:
        pentagram(1,distance)
        distance = distance + 10
    turtle.exitonclick()
if __name__ == '__main__':
     main()