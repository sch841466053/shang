from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from app01.models import Event, Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    return render(request, "index.html")


def login_action(request):

    if request.method == "POST":
         username = request.POST.get("username")
         password = request.POST.get("password")
         user = auth.authenticate(username=username,password=password)
         if user:
             auth.login(request,user)
             request.session["user1"] = username
             return redirect("/event_manage/")


# if username == "admin" and password == "admin123":
#              response = redirect("/event_manage/")
#              # response.set_cookie("user",username,3600)
#              request.session["user"] = username
#              return response
#
#
    return render(request,"index.html",{"error": "登录名或者密码错误"})
#

@login_required
def event_manage(request):
    event_list = Event.objects.all()
    username = request.session.get("user1")

    # username = request.COOKIES.get("user")
    # username = request.session.get("user1")
    return render(request,"event_manage.html", {"user": username, "events": event_list})

@login_required
def search_name(request):
    username = request.session.get("user1")
    search_name = request.GET.get("name")
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request,"event_manage.html",{"user":username, "events":event_list})


@login_required
def guest_manage(request):
    username = request.session.get("user1")
    guest_list = Guest.objects.all()
    p = Paginator(guest_list, 2)
    page = request.GET.get("page")
    print(page)
    try:
        contacts = p.page(page)
    except PageNotAnInteger:
        contacts = p.page(1)
    except EmptyPage:
        contacts = p.page(p.num_pages)

    return render(request,"guest_manage.html",{"user": username, "guests": contacts})


@login_required
def sign_index(request):
    id1 = request.GET.get("id")
    event = Event.objects.filter(id=id1)[0]
    return render(request, "sign_index.html", {"event": event})


@login_required
def sign_index_action(request,id2):
    event = Event.objects.filter(id=id2)[0]
    phone = request.POST.get("phone")
    print(phone)
    guest = Guest.objects.filter(phone=phone)
    print(guest)
    if guest:
        guest = Guest.objects.filter(phone=phone,event_id=id2)[0]
    else:
        return render(request,"sign_index.html", {"hint": "电话错误", "event": event})
    if not guest:
        return render(request,"sign_index.html", {"event": event, "hint": "电话或者会议错误"})
    if guest.sign:
        return render(request,"sign_index.html", {"event": event, "hint": "用户已经登记"})
    else:
        Guest.objects.filter(phone=phone,event_id=id2).update(sign="1")
        return render(request,"sign_index.html", {"event": event, "hint": "登记成功", "user":guest})


@login_required
def logout(request):
    auth.logout(request)
    return redirect("/index/")