from django.shortcuts import render
from app1.forms import EmployeeForm
from app1.models import Employee
from django.http import HttpResponseRedirect
# Create your views here.

# deleting Employee Details
'''
def input_view(request):
    if request.method == "GET":
        eno = request.GET.get('empno')
        emp = Employee.objects.get(empno = eno)
        form = EmployeeForm(instance = emp)
        return render(request, 'app1/employee.html', context={"form": form})
    
    elif request.method == "POST":
        emp = Employee.objects.get(empno = request.POST.get('empno'))
        emp.delete()
        return render(request, 'app1/input.html', context={})

def delete_view(request):
    return render(request, 'app1/input_emp.html')
'''

# Adding Employee Details in Database

'''
def view_empform(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit = True)

    response = render(request, 'app1/employee.html', context={"form": form})
    return response
'''
# Updating Employee Details

def list_emp(request):
    emp = Employee.objects.all()
    return render(request, 'app1/list_emp.html', context={'emp': emp})

def edit_view(request, empno):
    if request.method == "GET":
        emp = Employee.objects.get(empno = empno)
        form = EmployeeForm(instance= emp)
        return render(request, 'app1/employee.html', context={'form': form})
    
    elif request.method == "POST":
        emp = EmployeeForm(request.POST)
        emp.save(commit = True)
        return HttpResponseRedirect('list')