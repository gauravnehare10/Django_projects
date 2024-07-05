from django.shortcuts import render

# Create your views here.
def test_view(request, age):
    return render(request, "app1/find.html", context={'age': age})