import socket
# socket.AF_INET 指定不用电脑通信,socket.SOCK_STREAM 指定创建TcP套接字
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 访问百度
s.connect(('www.baidu.com',80))

#传输数据需要以字节传输,发送数据
s.send(b'hello')

#接收数据,限定接收的字节
connect= s.recv(2014)
print(connect)
s.close()