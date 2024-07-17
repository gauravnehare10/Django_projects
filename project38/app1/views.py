from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from app1.models import Marks
# Create your views here.

class GreetView(View):
    def get(self, request):
        msg = "Hello, Welcome to Class Based Views"
        response = HttpResponse(msg)
        return response
'''  
class DetailsView(View):
    def get(self, request):
        qs = Marks.objects.all()
        return render(request, 'app1/detailsview.html', context={'qs': qs})
''' 
class DisplayTemplateView(TemplateView):
    template_name = 'app1/hello.html'

class MarksView(ListView):
    model = Marks      # Automatically create template_name = "marks_list.html"
                       # And context_object_name = 'marks_list'
class CMarksView(ListView):
    model = Marks
    template_name = 'app1/cmarks_list.html'
    context_object_name = 'cmarks_list'

class FMarksView(ListView):
    template_name = 'app1/cmarks_list1.html'
    context_object_name = 'cmarks_list'
    def get_queryset(self):
        qs = Marks.objects.values('rollno', 'name')
        return qs

class DMarksView(DetailView):
    model = Marks
    template_name = 'app1/cmarks_list2.html'
    context_object_name = 'cmarks_list'
    pk_url_kwarg = 'pk'