'''
作者：赵宗召
时间：2017/11/28
功能：判断密码长度
面向对象编程，定义一个possword工具类
'''

class PasswordTool:
     '''
      密码工具类
     '''
     def __init__(self,password):
         #类的属性
         self.password = password
         self.trength_lve1 = 0

     def process_password(self):
          #密码判断规则
          if len(self.password) >= 8:
              self.trength_lve1 += 1
          else:
              print('密码长度不能小于8位')
          if self.check_alphu_exist():
              self.trength_lve1 += 1
          else:
              print('密码需要包含数字')
          if self.check_number_exist():
              self.trength_lve1 += 1
          else:
              print('密码需要包含字母')


      #类的方法

     def check_alphu_exist(self):
         '''判断字符串中是否含有字母'''
         has_number = False
         for i in self.password:
             if i.isalpha():
                 has_number = True
                 break
         return  has_number

     def check_number_exist(self):
         '''判断字符串中是否含有数字'''

         has_numberv = False
         for i in self.password:
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
             # 实例化对象
             password_tool = PasswordTool(password)
             password_tool.process_password()

             strength = password_check(password_tool.trength_lve1)
             f = open('password_5.0.txt', 'a')
             f.write('密码{}，密码强度{} 是否合格{}\n'.format(password,password_tool.trength_lve1,strength))
             f.close()
             if password_tool.trength_lve1 >= 3:
                 print('密码强度合规')
                 break
             else:
                 print('密码强度不合格')
             number -= 1
         if number == 0:
              print('您输入的密码次数过多')
if __name__ == '__main__':
         main()