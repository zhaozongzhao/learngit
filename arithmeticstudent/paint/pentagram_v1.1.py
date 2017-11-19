''''
   作者：赵宗召
   功能：绘制五角星
   版本：v1.1
   时间：2017.11.18
   功能：turtle库常用函数
   V1.1 新增功能：使用循环画五角星

'''
import turtle


def main():
    """
    主函数
    """
    count=1
    distance=200
    count1=1
    while count1<=5:
        while count<=5:
            turtle.forward(distance)
            turtle.right(144)
            count = count + 1
        count1 = count1 + 1
        distance = distance - distance / 4
        count = 1
        print(distance,count)
    turtle.exitonclick()
if __name__ == '__main__':
     main()