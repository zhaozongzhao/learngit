import time

ticks  = time.time()
print('当前时间戳',ticks)

#获取当前时间
localtime = time.localtime(time.time())
print('本地时间',localtime)

#格式化时间
localtime = time.asctime(time.localtime(time.time()))
print('本地时间',localtime)


#格式化日期
print(time.strftime('%Y-%m-%d  %H:%M:%S',time.localtime()))