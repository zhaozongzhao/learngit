# # while True:
#     try:
#         x =  int(input('请输入数字'))
#     except ValueError:
#         print('结束跳出')
#
#
# #一个try可以包含多个except
#
# while True:
#     try:
#         x =  int(input('请输入数字'))
#     except ValueError:
#         print('结束跳出')
#     except KeyboardInterrupt:
#         print('硬性跳出')

#一个except包含多个异常

# while True:
#     try:
#         x = int(input('请输入数字'))
#     except (ValueError,KeyboardInterrupt):
#         raise
#
# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except (ValueError) as Argument:
        print ("参数没有包含数字\n", Argument)

# 调用函数
temp_convert("xyz");