from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,'index.html')

def login_action(requrst):
    if requrst.method == 'POST':
        username =  requrst.POST.get('username','')
        password =  requrst.POST.get('password','')
        user =  auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(requrst,user) #登陆
            # return HttpResponse('成功')
            response = HttpResponseRedirect('/event_manage/')
           # response.set_cookie('user',username,3600)  #添加浏览器cookie
            requrst.session['user'] =  username #session信息记录
            return response
        else:
            return render(requrst,'index.html',{'error':'错误'})
@login_required()
def event_manage(request):
    # username = request.COOKIES.get('user','') 读取浏览器cookies
    username = request.session.get('user','') #读取浏览器session
    return render(request,'event_manage.html',{'user':username})