'''
作者：赵宗召
时间：2017/11/28
功能：判断密码长度

'''
def check_alphu_exist(password_str):
    '''判断是否又字母'''
    has_number = False
    for i in password_str:
        if i.isalpha():
            has_number = True
            break
    return  has_number


def check_number_exist(password_str):
    '''判断是否有数字存在'''

    has_numberv = False
    for i in password_str:
        if i.isnumeric():
            has_numberv = True
            break
    return has_numberv

def password_check(strength_lve1):
    has_hege = False
    if strength_lve1 < 3:
        pass
    else:
        has_hege = True
    return has_hege




def main():
    '''
     主函数
    '''
    # 设置密码次数
    number = 5
    while number > 0:
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
        strength = password_check(strength_lve1)
        f = open('password_3.0.txt', 'a')
        f.write('密码{}，密码强度{} \n'.format(password, strength))
        f.close()
        if strength_lve1 >= 3:
            print('密码强度合规')
            break
        else:
            print('密码强度不合格')
        number -= 1
    if number == 0:
         print('您输入的密码次数过多')



    

if __name__ == '__main__':
    main()