from django.shortcuts import render
from app1.forms import ContactForm
from django.http import HttpResponse
# Create your views here.

def contact_view(request):
    if request.method == "GET":
        form = ContactForm()
        return render(request, 'app1/contact.html', context={"form": form})
    
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            contactid = form.cleaned_data["contactid"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            
            string = ""
            for k, v in form.cleaned_data.items():
                string = string + f"<br>{k} --> {v}"
            return HttpResponse(string)
        else:
            return render(request, 'app1/contact.html', context={"form":form})
        