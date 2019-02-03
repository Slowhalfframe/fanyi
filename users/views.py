from django.shortcuts import render, HttpResponse
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect   # 路由重定向
from django.contrib.auth.models import User     # 内置用户
from django.contrib.auth import authenticate, login, logout     # 内置的用户认证
from django.contrib.auth.decorators import login_required       # 登录检查
from itsdangerous import TimedJSONWebSignatureSerializer
from . import models
from . import tools
from io import BytesIO  # 在内存中读写bytes
from . import zsend_email
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'second_Edition.settings'


# 登录
def user_login(request):
    if request.method == 'GET':
        try:
            next_url = request.GET['next']
        except:
            next_url = "/work/"

        print(next_url)
        return render(request, 'users/sign_in.html', {"next_url": next_url})
        # return render(request, 'users/sign_in.html', {})
    if request.method == 'POST':
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        islong = request.POST.get("islong", "no")
        next_url = request.POST.get("next", "/work/")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session["LoginUser"] = user
                if islong == "on":
                    request.session.set_expiry(3600 * 24 * 7)
                elif islong == "":
                    request.session.set_expiry(0)
                return redirect(next_url)

            else:
                return render(request, 'users/sign_in.html', {"msg": "未激活"})
        else:
            return render(request, 'users/sign_in.html', {"msg": "账户、密码错误或账户未激活"})


# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html', {})
    if request.method == 'POST':
        username = request.POST['username'].strip()
        email = request.POST['email'].strip()
        password = request.POST['password'].strip()
        querenpassword = request.POST['confirm_password'].strip()
        code = request.POST['code']
        # 后台验证
        if code.upper() != request.session['code'].upper():
            return render(request, 'users/register.html', {"msg": "验证码不正确，请重新注册"})
        if len(password) < 6:
            return render(request, 'users/register.html', {"msg": "密码长度不足6位，请重新注册"})
        if password != querenpassword:
            return render(request, 'users/register.html', {"msg": "两次输入密码不一致，请重新注册"})
        try:
            # 用户名验证
            User.objects.get(email=email)
            return render(request, 'users/register.html', {"msg": "用户名已存在，请重新注册"})
        except:
            try:
                # create_user辅助函数创建用户
                user = User.objects.create_user(password=password, username=username, email=email, is_active=0)
                usera = models.users_more_info(user=user)
                user.save()
                usera.save()
                # 发送验证邮件
                print("发送邮件")
                zsend_email.mail(user.email, user.id)
                # return render(request, "user/tiaozhuan.html", {"msg": "恭喜注册成功，请登录"})
                return redirect('/users/tips')
            except:
                return render(request, "users/register.html", {"msg": "注册失败，请重新注册"})


# 验证码 函数
def code(request):
    img, code = tools.create_code()
    # 首先需要将code 保存到session 中
    request.session['code'] = code
    # 返会图片
    file = BytesIO()
    img.save(file, 'PNG')

    return HttpResponse(file.getvalue(), "image/png")


# ajax验证邮箱
def checkemail(request, email):
    try:
        User.objects.get(email=email)
        return JsonResponse({"msg": "此邮箱已注册，请重新输入", "success": False})
    except:
        return JsonResponse({"msg": "邮箱可用，请继续输入", "success": True})


# ajax验证邮箱
def checkusername(request, username):
    try:
        User.objects.get(username=username)
        return JsonResponse({"msg": "此昵称已注册，请重新输入", "success": False})
    except:
        return JsonResponse({"msg": "昵称可用，请继续输入", "success": True})


# 邮箱链接激活
def email_verification(request, token):
    SECRET_KEY = 's(do(h$i-d3rzrx7yhw@ik!cgwg+52-c#roc*3gk#wfk2y@1=2'
    s = TimedJSONWebSignatureSerializer(SECRET_KEY, expires_in=3600*64)
    try:
        data = s.loads(token)
        id = data["confirm"]
        print(id)
        user = User.objects.get(pk=id)
        user.is_active = 1
        user.save()
        return redirect('/users/')
    # 验证失败，会抛出异常
    except:
        print("over")
        return HttpResponse('激活链接已过期')


    # 注册之后跳转提示界面
def tips(request):
    return render(request, 'users/tips.html', {})


# ajax验证验证码
def checkcode(request, code):
    s_code = request.session['code']
    if s_code.upper() != code.upper():
        return JsonResponse({"msg": "验证码错误，请重新填写", "success": False})
    else:
        return JsonResponse({"msg": "验证码正确，请注册", "success": True})


# 退出登录
@login_required
def user_logout(request):
    logout(request)
    return redirect('/')


# 个人主页
@login_required
def user_info(request, id):
    user = models.users_more_info.objects.get(user=id)
    return render(request, 'users/user_info.html', {'user_info':user_info})


# 修改密码
@login_required
def change_pwd(request):
    old_pwd = request.POST['old_pwd'].strip()
    new_pwd = request.POST['new_pwd'].strip()
    new_pwd2 = request.POST['new_pwd2'].strip()
    print(old_pwd, new_pwd, new_pwd2)

    user = User.objects.get(pk=request.user.id)
    user = authenticate(username=user.username, password=old_pwd)
    if user is None:
        return redirect(request, 'users/user_info.html', {'script': "alert", 'wrong': '输入的旧密码不正确'})
    else:
        if new_pwd != new_pwd2:
            return render(request, 'users/user_info.html', {'script': "alert", 'wrong': '两次输入的密码不相同'})
            # return HttpResponseRedirect('/users/'+str(user.id)+'/user_info?script=alert&wrong=两次输入的密码不相同')
        else:
            user.set_password(new_pwd)
            user.save()
            user_logout(request)
            return redirect('/users/')
            # except:
            #     return render(request, 'users/user_info.html', {'script': "alert", 'wrong': '修改密码失败'})


# ajax验证旧密码
@login_required
def check_password(request, old_pwd):
    u = User.objects.get(pk=request.user.id)
    print(u)
    print(u.username)
    user = authenticate(username=u.username, password=old_pwd)
    if user is None:
        return JsonResponse({"msg": "输入的旧密码不正确", "success": False})
    else:
        return JsonResponse({"msg": "", "success": True})


def change_username(request, username):
    # ajax实现修改昵称
    user = User.objects.get(pk = request.user.id)
    if len(username) != 0:
        user.username = username
        user.save()
        return JsonResponse({"msg": "", "success": True})


def change_email(request, email):
    # ajax实现修改邮箱
    pass

    # 参考验证旧密码，路由还没有配  \W+