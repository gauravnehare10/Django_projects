from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'app1/calc.html')

def calculator(request):
    a = request.GET.get('t1')
    b = request.GET.get('t2')
    opr = request.GET.get('opr')
    match opr:
        case '+':
            res = eval(a) + eval(b)
        case '-':
            res = eval(a) - eval(b)
        case '*':
            res = eval(a) * eval(b)
        case '/':
            res = eval(a) / eval(b)
        case _:
            res = None
    result = {'res': res}
    return render(request, 'app1/result.html', context=result)
