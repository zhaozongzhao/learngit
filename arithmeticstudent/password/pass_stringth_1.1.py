'''
作者：赵宗召
时间：2017/11/28
功能：判断密码长度
限制密码次数
'''
def check_alphu_exist(password_str):
    '''判断是否又字母'''

    for i in password_str:
        if i.isalpha():
            return  True
    return  False


def check_number_exist(password_str):
    '''判断是否有数字存在'''
    for i in password_str:
        if i.isnumeric():
            return True
    return False

def password_check():
    # 输入的密码
    password = input('请输入密码')
    # 密码强度的变量
    strength_lve1 = 0

    # 密码长度大于8
    if len(password) >= 8:
        strength_lve1 += 1
    else:
        print('密码长度不能小于8位')
    if check_number_exist(password):
        strength_lve1 += 1
    else:
        print('密码需要包含数字')
    if check_alphu_exist(password):
        strength_lve1 += 1
    else:
        print('密码需要包含字母')
    if strength_lve1 >= 3:
        print('密码强度合规')
    else:
        print('密码强度不合格')




def main():
    '''
     主函数
    '''
    # 设置密码次数
    number = 0
    while number<5:
        password_check()
        number+=1


    

if __name__ == '__main__':
    main()