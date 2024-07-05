from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    output = "<h1>This is Index Page</h1>"
    response = HttpResponse(output)
    return response

def home(request):
    output = "<h1>This is Home View</h1>"
    response = HttpResponse(output)
    return response
