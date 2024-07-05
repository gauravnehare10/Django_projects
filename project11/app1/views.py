from django.shortcuts import render

# Create your views here.
def add(request, num1, num2):
    result = eval(num1) + eval(num2)
    d = {'num1': num1, 'num2': num2, 'result': result}
    return render(request, 'app1/result.html', context=d)