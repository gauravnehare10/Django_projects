from django.shortcuts import render

# Create your views here.
def disp_view(request, n):
    if n == 1:
        return render(request, "app1/child1.html")
    elif n == 2:
        return render(request, "app1/child2.html")