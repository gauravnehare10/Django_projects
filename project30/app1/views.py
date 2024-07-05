from django.shortcuts import render
from app1.models import Register
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'app1/index.html')

def register(request):
    name = request.POST.get('name')
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    try:
        Register.objects.create(name = name, user = user, password = pwd)
        res = HttpResponse('<h2>User Registered</h2>')
        return res
    except:
        res = HttpResponse('<h2>Error in Registeration</h2>')
        return res

def login_template(request):
    return render(request, 'app1/login.html')

def login(request):
    user = request.GET.get('user')
    pwd = request.GET.get('pwd')
    
    try:
        Register.objects.get(user = user, password = pwd)
        res = HttpResponse(f'<h2>{user}, Welcome</h2>')
    except:
        res = HttpResponse(f'<h2>Invalid username or password<h2>')

    return res

def update_template(request):
    return render(request, 'app1/updatepass.html')

def update_password(request):
    uname = request.POST.get('user')
    opwd = request.POST.get('opwd')
    npwd = request.POST.get('npwd')
    
    try:
        obj = Register.objects.get(user=uname, password=opwd)
        obj.password = npwd
        obj.save()
        res = HttpResponse("<h2>Password Updated</h2>")

    except:
        res = HttpResponse("<h2>Invalid Username or Password</h2>")

    return res

def delete_template(request):
    return render(request, 'app1/deleteuser.html')

def delete_user(request):
    user = request.POST.get('user')
    try:
        obj = Register.objects.get(user = user)
        obj.delete()
        obj.save()
        res = HttpResponse("<h2>User Deleted</h2>")
    
    except:
        res = HttpResponse("<h2>Invalid Username<h2>")
    return res