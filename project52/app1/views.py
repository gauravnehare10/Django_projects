from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def profile_view(request):
    return render(request, 'app1/profile.html', context={'user': request.user})


def index(request):
    return render(request, 'app1/index.html')