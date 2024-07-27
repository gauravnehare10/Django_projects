from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'app1/index.html')

def view1(request):
    c = request.COOKIES.get('count', 0)
    if c == 0:
        msg = f'''<h2>Hello, {request.GET.get('name')}</h2>
        <a href='/view1/'>Index</a>'''
        c = c + 1
        response = HttpResponse(msg)
        response.set_cookie('count', c)
        return response
    else:
        msg = f'''<h2>Welcome Back, {request.GET.get('name')}</h2>
        <a href='/view1/'>Index</a>'''
        response = HttpResponse(msg)
        return response
