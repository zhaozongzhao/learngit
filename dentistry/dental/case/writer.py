# import  time,csv
# import  os,sys
# from itertools import islice
# from threading import Timer
#
# h  = ['确认预约 |爽约 |核销卡券 |上传影像 |下载影像|完成就诊', '北京欢乐丽格口腔诊所有限公司', '解玢', '15811128087',
#       '2110***3327', '', '成人', '已取消', '未上传', '', '', '', '', '--', '', '', '', '', '', '', '', '', '', '', '', ''
#       '确认预约 |爽约 |核销卡券 |上传影像 |下载影像|完成就诊', '上海首尔丽格医疗美容医院有限公司', '李震', '13917911112', '3101***0513', '', '成人', '已取消', '未上传', '', '', '', '', '--', '', '', '', '', '', '', '', '', '', '', '', '']
#
# def get_current_path(file_name):
#     #获取当前目录
#     base_dir = os.path.dirname(__file__)
#     base_dir = str(base_dir)
#     #将路径中的\\用\取代
#     base = base_dir.replace('\\','/')
#     file_path = base +'/data/'+file_name
#     return  file_path
# #
# # with open(get_current_path(''),mode='r',encoding='utf-8',newline= '') as f:
# #         reder = csv.reader(f)
# #         for i in  reder:
# #             print(i)
# #
# # def writr_csv_file(list_data):
# #     print('写入次数')
# #     #csv文件写入
# #     try:
# #       lines = list_data
# #       print(lines)
# #       filename =time.strftime('%Y-%m-%d',time.localtime(time.time()))+ '.csv'
# #       with open(filename,encoding='utf-8',mode='a',newline='') as somefile:
# #           writer = csv.writer(somefile)
# #           writer.writerow(lines)
# #     except Exception as a:
# #         print('写入错误',a)
# #
#
# def writr_csv_file(list_data):
#     print('写入次数')
#     #csv文件写入
#     try:
#       lines = list_data
#       filename =time.strftime('%Y-%m-%d',time.localtime(time.time()))+ '.csv'
#       file_name = get_current_path(filename)
#       with open(file_name,mode='a',encoding='utf-8',newline='') as somefile:
#           writer1 = csv.writer(somefile)
#           writer1.writerow(lines)
#
#     except Exception as a:
#         print('写入错误',a)
# # i=0
# # while i < 1:
# #  writr_csv_file('123456')
# #  i+=0.5
#
# def read_csv():
#     '''读取文件'''
#     filename =time.strftime('%Y-%m-%d',time.localtime(time.time()))+ '.csv'
#     file_name = get_current_path(filename)
#     dats = csv.reader(open(file_name,encoding='utf-8',mode='r'))
#     for user in dats:
#         return user
#
# def list_data_get():
#
#    list_data=['确认预约 |爽约 |核销卡券 |上传影像 |下载影像|完成就诊', '北京欢乐丽格口腔诊所有限公司', '解玢', '15811128087',
#       '2110***3327', '', '成人', '已取消', '未上传', '', '', '', '', '--', '', '', '', '', '', '', '', '', '', '', '', '']
#    writr_csv_file(list_data)
#
#
#
# def is_phone(phone):
#      old_phone =read_csv()[3]
#      new_phone = phone
#      if old_phone == new_phone:
#          print('没有新的患者')
#      elif old_phone == '' or new_phone == '':
#          print('手机号码获取错误')
#      else:
#          list_data_get()
#
#
# def delete_file():
#     #删除文件
#     filename =time.strftime('%Y-%m-%d',time.localtime(time.time()))+ '.csv'
#     file_name = get_current_path(filename)
#     os.remove(file_name)
#
#
# import logging
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
#
# # def printHello():
# #     print( "Hello World"  )
# #     t = Timer(10, printHello)
# #     t.start()
# #
# # printHello()
#
# logging.basicConfig(filename=os.path.join(os.getcwd(),'log.txt'),level=logging.DEBUG)
# logging.debug('this is a message')