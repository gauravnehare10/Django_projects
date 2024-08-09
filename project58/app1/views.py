from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
# Create your views here.
def student_view(request):
    student_data = {'rollno': 101,
                    'name': 'naresh',
                    'course': 'python',
                    'fee': 5000}
    response =JsonResponse(student_data)
    return response

def student_view1(request):
    student_data = {'rollno': 101,
                    'name': 'naresh',
                    'course': 'python',
                    'fee': 5000}
    json_data = json.dumps(student_data)
    response = HttpResponse(json_data, content_type='application/json')
    return response

def student_view2(request, rollno):
    student_data = [{'rollno': 1,
                    'name': 'naresh'},
                    {'rollno': 2,
                    'name': 'suresh'},
                    {'rollno': 3,
                    'name': 'kishor'}]
    flag = False
    for data in student_data:
        if data['rollno'] == rollno:
            response = JsonResponse(data)
            flag = True
            break
    
    if flag:
        return response
    else:
        d = {'Error': 'Invalid Roll No'}
        response = JsonResponse(d)
        return response