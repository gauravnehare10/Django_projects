from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse
from app1.models import Marks
# Create your views here.

class GreetView(View):
    def get(self, request):
        msg = "Hello, Welcome to Class Based Views"
        response = HttpResponse(msg)
        return response
    
class DetailsView(View):
    def get(self, request):
        qs = Marks.objects.all()
        return render(request, 'app1/detailsview.html', context={'qs': qs})
    
class DisplayTemplate(TemplateView):
    template_name = 'app1/hello.html'
