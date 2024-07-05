from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import *
# Create your views here.

def test_view(request):
    test = TestForm()
    return render(request, 'app1/test_temp.html', context={'test':test})

def read_view(request):
    b = request.GET.get('test_field1')
    c = request.GET.get('test_field2')
    d = request.GET.get('test_field3')
    e = request.GET.get('test_field4')
    return HttpResponse(f'<h1>{b}, {c}, {d}, {e}</h1>')