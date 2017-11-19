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
   v4.0  树形图

'''
import  turtle

def tree_pentagram(distance):

    if distance > 5:
        # 绘制右侧树枝

        #画右侧
        turtle.forward(distance)
        print('向前',distance)
        turtle.right(20)
        print('向右20度')
        tree_pentagram(distance-10)
        print('向前', distance-10 )

        #左侧
        turtle.left(40)
        print('向左20度')
        tree_pentagram(distance - 10)
        print('向前', distance-10)

        #回到之前的位置
        turtle.right(20)
        print('向右20度')
        turtle.backward(distance)




def main():
    """
    主函数
    """
    turtle.left(90)
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.pensize(5)
    turtle.pencolor("green")
    tree_pentagram(100)
    turtle.exitonclick()


if __name__ == '__main__':
     main()