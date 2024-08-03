from django.shortcuts import render, redirect
from django.http import HttpResponse
from app1.forms import UserForm

# Create your views here.
'''
def home(request):
    response = "<h2>Welcome</h2>"
    return HttpResponse(response)

'''
    
def home(request):
    return render(request, 'registration/logout.html')

def signup(request):
    if request.method == "GET":
        form = UserForm()
        return render(request, 'registration/signup.html', context={'form': form})
    
    else:
        form = UserForm(request.POST)
        form.save()
    redirect('/')
