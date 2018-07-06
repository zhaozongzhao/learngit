import requests

path = 'https://www.douban.com/'
#请求豆瓣首页
r = requests.get('https://www.douban.com/')
print(r.status_code) #判断状态

#get请求中添加参数
r = requests.get(path,params={'q':'python','cat':'1001'})
print(r.status_code) #判断状态
print(r.text) #文本
print(r.encoding) #检测编码
print(r.content) #获取字节对象

#传入http Header
r = requests.get(path,headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like'
                                               ' Mac OS X) AppleWebKit'})
print(r.text) #文本

r = requests.post('https://accounts.douban.com/login',
                 data={'form_email': 'abc@example.com', 'form_password': '123456'})
print(r.headers) #获取响应头
print(r.cookies['ts']) #查看cookis
