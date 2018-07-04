from datetime import datetime,timedelta
now =  datetime.now()
print(now)
#加一个小时
print(now + timedelta(hours=1))
#加一天
print(now + timedelta(days=1))
#减一天
print(now - timedelta(days=1))
#加一天两个小时
print(now + timedelta(days=1,hours=2))