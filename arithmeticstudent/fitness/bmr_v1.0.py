'''
作者：赵宗召
时间：2017年11月20
版本：1.0
新增功能：bmr基础代谢率的计算

'''



def Bmr():
    # 性别
    gender = input('请输入您的性别(按Q退出)： ')
    # 体重(kg)
    weight = input('请输入您的体重(按Q退出)： ')
    # 身高
    height = input('请输入您的身高(按Q退出)： ')
    # 年龄
    age = input('请输入您的年龄(按Q退出)： ')

    if gender == '男':
        # 男性
        bmr = 13.7 * eval(weight) + 5.0 * eval(height) + 6.8 * eval(age) + 66
    elif gender == '女':
        # 女性
        bmr = 9.6 * weight + 1.8 * height + 4.7 * age + 655
        print(bmr)
    else:
        bmr = -1

    if bmr != -1:
        print("你的基础代谢率为： ", bmr)
    else:
        print('您的性别有误')

def main():
    """
    主函数
    """
    Bmr()


if __name__ == '__main__':
    main()
