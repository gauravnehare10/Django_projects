from django.shortcuts import render

# Create your views here.

def cart(request):
    b = request.GET.get('btn')
    if b == "Add":
        response =  render(request, 'app1/index.html', context = {'opr': 'Add'})
        pname = request.GET.get('pname')
        qty = request.GET.get('qty')
        response.set_cookie(pname, qty)
        return response
    
    elif b == "Update":
        response =  render(request, 'app1/index.html', context = {'opr': 'Update'})
        pname = request.GET.get('pname')
        qty = request.GET.get('qty')
        response.set_cookie(pname, qty)
        return response
    
    elif b == "Delete":
        response =  render(request, 'app1/index.html', context = {'opr': 'Delete'})
        pname = request.GET.get('pname')
        qty = request.GET.get('qty')
        response.set_cookie(pname, qty, max_age=0)
        return response
    
    elif b == "View":
        product = request.COOKIES
        response = render(request, 'app1/index.html', context = {'product': product})
        return response