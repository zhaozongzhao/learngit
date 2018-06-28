#内存读写
from io import StringIO
f = StringIO()
f.write('hello')
print(f.getvalue()) # getvalue()方法用于获取写入后的str


from  io import BytesIO
f = BytesIO('中文'.encode('utf-8'))
print(f.read())


data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8')
f = BytesIO(data)
print(f.read())

