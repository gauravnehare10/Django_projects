from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, TemplateView
from app1.models import *
from django.http import HttpResponse
# Create your views here.

class EmployeeList(ListView):
    context_object_name = 'emp'
    template_name = 'app1/employee_list.html'
    def get_queryset(self):
        qs = Employee.objects.select_related('deptno')
        return qs
    
class EmployeeUpdate(UpdateView):
    def post(self, request, *args, **kwargs):
        deptno = request.POST.get('deptno')
        update_sal = float(request.POST.get('upd_sal'))
        qs = Employee.objects.filter(deptno = deptno)
        for emp in qs:
            emp.salary = emp.salary + update_sal
            emp.save()
        msg = 'Updated'
        return render(request, 'app1/update_emp.html', context={'msg': msg})
    
class UpdateEmpTemp(TemplateView):
    template_name = 'app1/update_emp.html'

