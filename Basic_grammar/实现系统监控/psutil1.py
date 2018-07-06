import psutil
#获取cpu的信息
print(psutil.cpu_count())  #cpu逻辑数量
print(psutil.cpu_count(logical=False)) #cpu物理核心

#统计cpu用户/系统/空闲时间
print(psutil.cpu_times())

#cpu使用率
print(psutil.cpu_percent(interval=1,percpu=True))


#获取内存信息
print(psutil.virtual_memory())
print(psutil.swap_memory())

#获取磁盘信息
#获取磁盘分区信息
print(psutil.disk_partitions())
#磁盘使用情况
print(psutil.disk_usage('/'))
#磁盘IO
print(psutil.disk_io_counters())


#获取进程信息

print(psutil.pids()) #所有进程的id
p = psutil.Process(12001)

print(p.name()) #进程名称
print(p.exe())  #进程路径
print(p.cwd())  #进程工作目录
print(p.cmdline()) #进程启动名利行
print(p.ppid()) #父进程ID
print(p.parent()) #父进程
print(p.children()) #子进程列表

