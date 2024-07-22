from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from app1.models import Student

# Create your views here.

class HomeView(TemplateView):
    template_name = 'app1/base.html'

class CourseListView(ListView):
    model = Student
    fields = '__all__'
    context_object_name = 'students'
    template_name = 'app1/student_list.html'
    def get_queryset(self):
        course = self.request.GET.get('course')
        qs = Student.objects.filter(course = course)
        return qs
    