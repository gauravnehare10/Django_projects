from django.shortcuts import render

# Create your views here.
def test_view(request, name, marks):
    return render(request, 'app1/find.html', context={'name': name, 'marks': marks})
