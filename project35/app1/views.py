from django.shortcuts import render
from app1.forms import *
from django.http import HttpResponse
# Create your views here.

def view1(request):
    if request.method == "GET":
        form = TransactionForm()
        return render(request, 'app1/temp1.html', context={'form': form})
    
    elif request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            return HttpResponse("Valid")
        else:
            return render(request, 'app1/temp1.html', context={'form': form})