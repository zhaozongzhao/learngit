#从wsgiref模块导入
from wsgiref.simple_server import  make_server
#导入自己编写的applcation
from Basic_grammar.web开发.hello import application

#创建一个服务器
httpd = make_server('',8000,application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()