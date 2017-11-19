''''
   作者：赵宗召
   功能：绘制五角星
   版本：v1.0
   时间：2017.11.18
   功能：turtle库常用函数
'''
import turtle

def main():
    """
    主函数
    """
    #画笔向前移动50像素
    turtle.forward(100)

    #画笔向后移动50个像素
    turtle.backward(50)

    #画笔向左移动50像素
    turtle.left(50)

    #画笔向右移动50个像素
    turtle.right(20)

    #点击关闭图形窗口
    turtle.exitonclick()

    #抬起画笔，之后移动不会绘制图形
    turtle.penup()

    #放下画笔，之后移动会绘制图形
    turtle.pendown()

    #设置画笔宽度
    turtle.pensize()

    #设置画笔颜色

    turtle.pencolor()




if __name__ == '__main__':
     main()