from django.shortcuts import render

# Create your views here.
def test_view(request):
    a = 10  # Local Variable
    b = 20  # Local Variable
    c = a + b
    d = {'a':a, 'b':b, 'c':c}
    return render(request, 'app1/result.html', context=d)
