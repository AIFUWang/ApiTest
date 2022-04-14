from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def welcome(request):
    # return HttpResponse("欢迎欢迎，热烈欢迎！")
    return render(request, 'welcome.html')


#
# def home(request):
#     return render(request, 'welcome.html', {"whichHTML": "home.html", "oid": ""})

# 进入主页
def home(request):
    return render(request, 'welcome.html', {"whichHTML": "home.html", "oid": ""})


def login(request):
    return render(request, 'login.html')

def logout(request):
    from django.contrib import auth
    auth.logout(request)
    return HttpResponseRedirect('/login/')


def login_action(request):
    u_name = request.GET['username']
    p_word = request.GET['password']
    from django.contrib import auth
    user = auth.authenticate(username=u_name, password=p_word)
    if user is not None:
        # 进行正确操作
        return HttpResponse('成功')
    else:
        # 返回前端告诉前端用户名或密码不对
        return HttpResponse("失败")


def register_action(request):
    u_name = request.GET['username']
    p_word = request.GET['password']
    from django.contrib.auth.models import User
    try:
        user = User.objects.create_user(username=u_name, password=p_word)
        user.save()
        return HttpResponse("注册成功！")
    except:
        return HttpResponse("注册失败~用户名已存在~")


# 返回子页面
def child(request, eid, oid):
    return render(request, eid)
