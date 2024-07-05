from django.shortcuts import render

# Create your views here.
def display_img(request):
    return render(request, 'app1/test.html')