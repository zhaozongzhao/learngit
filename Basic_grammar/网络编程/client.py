import socket
import sys

#创建soket对象

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#获取本地主机名
host = socket.gethostname()

port = 9999

#连接服务,连接主机和端口
s.connect((host,port))

#接收小于1024字节的数据
msg = s.recv(1024)

s.close()

print(msg.decode('utf-8'))