from django.shortcuts import render
from app1.models import *
from app1.forms import *
# Create your views here.

def add_book(request):
    if request.method == "POST":
        form1 = AuthorForm(request.POST)
        form2 = BookForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            form1.save(commit=True)
            form2.save(commit=False)
            form2.author = form1
            form2.save(commit=True)

    form1 = AuthorForm()
    form2 = BookForm()
    forms = [form1, form2]
    return render(request, 'app1/add_book.html', context={'forms': forms})
