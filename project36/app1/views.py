from django.shortcuts import render
from app1.forms import EmployeeForm
# Create your views here.

def view_empform(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit = True)

    response = render(request, 'app1/employee.html', context={"form": form})
    return response

