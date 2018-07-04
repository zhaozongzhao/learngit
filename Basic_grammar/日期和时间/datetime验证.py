from datetime import datetime
now = datetime.now()
print(now)
print(type(now))

#获取指定日期和时间
dt = datetime(2015,4,19,12,20) #用指定的日期时间创建
print(dt)

print(dt.timestamp()) #datatime转换为timestamp

#将timestamp转换datetime,使用datatime提供的fromtimestamp()
import time

t = time.time()
print(datetime.fromtimestamp(t))


#字符串转换为datetime
cady = datetime.strptime('2015-6-1','%Y-%m-%d')
print(cady)

#datetime转化为str
now = datetime.now()
print(now.strftime('%Y:%H:%M'))