from flask import Flask
from flask  import request

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def home():
    return '<h1>HOME<h1>'


@app.route('/signin',methods = ['GET'])
def signin_from():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">登陆</button></p>
              </form>
              '''

@app.route('/signin',methods = ['POST'])
def signin():
    #需要从request对象读取表单内容
    if request.form['username'] == 'admin' and request.form['password'] == '123456':
         return '<h3>hello,admin<h3>'
    return '<h3>Bad username or password<h3>'

if __name__ == '__main__':
    app.run()