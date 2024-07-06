from django.shortcuts import render
from django.http import HttpResponse
from app1 import forms

# Create your views here.

def student_view(request):
    if request.method == "GET":
        form = forms.StudentForm()
        return render(request, "app1/student.html", context={'form': form})
    
    elif request.method == "POST":
        form = forms.StudentForm(request.POST)
        form.is_valid()
        string = f'''<h2>
        Roll No.: {form.cleaned_data.get('rollno')}<br>
        Name: {form.cleaned_data.get('sname')} <br>
        Course: {form.cleaned_data.get('course')}<br>
        Fees: {form.cleaned_data.get('fees')}<br>
        Remark: {form.cleaned_data.get('remark')}</h2>'''
        return HttpResponse(string)