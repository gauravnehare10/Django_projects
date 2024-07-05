from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    opr = request.GET.get('opr')
    match opr:
        case '+':
            res = eval(a)+eval(b)
        case '-':
            res = eval(a)-eval(b)
        case '*':
            res = eval(a)*eval(b)
        case '/':
            res = eval(a)/eval(b)
        case _:
            res = None

    result = {'res':res}
    return render(request, 'app1/result.html', context=result)