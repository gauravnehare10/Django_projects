from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
    response = HttpResponse("<h1>Inside View</h1>")
    return response