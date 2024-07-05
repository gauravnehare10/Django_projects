from django.shortcuts import render

# Create your views here.

def welcome(request):
    response = render(request, 'app1/welcome.html')
    return response
