''''
   作者：赵宗召
   功能：绘制五角星
   版本：v3.0
   时间：2017.11.19
   功能：turtle库常用函数
   V1.1 新增功能：使用循环画五角星
   v1.2 将画五角星封装成函数
   V2.0 设置画笔的颜色和宽度
   V3.0  循环和函数的结合，递归

'''
import turtle
#画五角星
def pentagram(count,distance):
    count = 1
    while count <= 5:
        turtle.forward(distance)
        turtle.right(144)
        count = count + 1

def recursion_pentagram(size):
    """
    重复画五角星形

    """
    count = 1
    while count <= 5:
        turtle.forward(size)
        turtle.right(144)
        count +=1
    size+=10
    if size<=100:
        recursion_pentagram(size)




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
    recursion_pentagram(20)

if __name__ == '__main__':
     main()