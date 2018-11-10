from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request,'index.html')

def login_action(requrst):
    if requrst.method == 'POST':
        username =  requrst.POST.get('username','')
        password =  requrst.POST.get('password','')
        if username == 'admin' and password == '111111':
            # return HttpResponse('成功')
            return  HttpResponseRedirect('/event_manage/')
        else:
            return render(requrst,'index.html',{'error':'错误'})

def event_manage(request):
    return render(request,'event_manage.html')