from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app1/index.html')

def cart(request):
    btn = request.POST.get('btn')
    print(btn)
    if btn == 'add':
        pname = request.POST.get('pname')
        qty = request.POST.get('qty')
        request.session[pname] = qty
        msg = 'add'

    elif btn == 'update':
        pname = request.POST.get('pname')
        qty = request.POST.get('qty')
        request.session[pname] = qty
        msg = 'update'

    elif btn == 'delete':
        pname = request.POST.get('pname')
        if pname in request.session:
            del request.session[pname]
            msg = 'delete'
        else:
            msg = 'notfound'

    elif btn == 'list':
        msg = 'list'

    return render(request, 'app1/index.html', context={'msg': msg})