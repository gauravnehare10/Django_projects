from django.shortcuts import render

# Create your views here.

class Employee:
    def __init__(self):
        self.eno = 101
        self.ename = "Naresh"
        self.salary = 5000

def test_view(request):
    course_list = ["PYTHON", "JAVA", ".NET", "ORACLE"]
    c = {'list1':course_list}
    return render(request, 'app1/result.html', c)

def empdetails(request):
    e = Employee()
    c = {'e': e}
    return render(request, 'app1/emp.html', context=c)
