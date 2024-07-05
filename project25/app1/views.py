from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login_template(request):
    return render(request, 'app1/login.html')

def login(request):
    users = {'nit':'nit123',
             'naresh':'n123',
             'suresh':'s567'}
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    msg = 'Sign in'
    if user in users and pwd == users[user]:
        msg = f'<h2>Hey {user}, Welcome back!!</h2>'
        response = HttpResponse(msg)
        return response
    else:
        msg = 'Invalid Username or Password'
        return render(request,'app1/login.html', context = {'msg':msg})
    