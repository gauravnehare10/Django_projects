from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
    output = "<h1>This is View1</h1>"
    response = HttpResponse(output)
    return response

def view2(request):
    output = "<h1>This is View2</h1>"
    response = HttpResponse(output)
    return response

def view3(request):
    return render(request, "app1/display.html")