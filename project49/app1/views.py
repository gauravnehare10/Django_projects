from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def get_max_age(request):
    a = request.session.get_session_cookie_age()
    response = HttpResponse(a)
    return response

def create_session(request):
    request.session['x'] = 10
    request.session.set_expiry(10)
    a = request.session.get_expiry_age()
    response = HttpResponse(a)
    return response

def get_data(request):
    x = request.session('x')
    response = HttpResponse(x)
    return response