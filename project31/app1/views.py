from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import LoginForm
# Create your views here.
def login_view(request):
    login = LoginForm()
    return render(request, "app1/login_temp.html", context={"login":login})

def display(request):
    return HttpResponse("<h2>Hello</h2>")