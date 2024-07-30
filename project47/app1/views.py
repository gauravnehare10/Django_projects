from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def verify_cookie(request):
    if request.method == "POST":
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            msg = "You are Logged In"
            return HttpResponse(msg)

        else:
            msg = "Please Enable Cookies"
            return HttpResponse(msg)
    
    request.session.set_test_cookie()
    return render(request, "app1/login_form.html")


def login_view(request):
    return render(request, 'app1/login_form.html')

def login(request):
    if 'uname' not in request.session:
        request.session['uname'] = request.GET.get('uname')
        return render(request, 'app1/inbox.html')
    else:
        response = HttpResponse('Your Logged in')
        return response
    
def inbox(request):
    pass