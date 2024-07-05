from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def stud_adm(request):
    output = "<h1>Student Admission View</h1>"
    response = HttpResponse(output)
    return response

def stud_info(request):
    output = "<h1>Student Info View</h1>"
    response = HttpResponse(output)
    return response
