from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'app1/index.html')

def view1(request):
    name = request.GET.get("name")
    link = '<a href="/view2/">Greeting</a>'
    response = HttpResponse(link)
    response.set_cookie("name", name)
    return response

def view2(request):
    name = request.COOKIES["name"]
    msg = f"Hello, {name}"
    response = HttpResponse(msg)
    return response