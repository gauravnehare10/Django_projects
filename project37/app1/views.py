from django.shortcuts import render, redirect
from app1.forms import MarksForm
from app1.models import Marks
from django.http import HttpResponse
# Create your views here.
def view_index(request):
    return render(request, 'app1/index.html')

def add_view(request):
    if request.method == "GET":
        form = MarksForm()
        return render(request, "app1/add_stud.html", context={"form": form})
    
    elif request.method == "POST":
        form = MarksForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            message = "Data Saved Successfully"
            return render(request, 'app1/add_stud.html', context={"form":form, "message": message})
        else:
            return render(request, "app1/add_stud.html", context={"form": form})

def list_marks(request):
    marks_data = Marks.objects.all()
    return render(request, 'app1/list_marks.html', context={'marks_data': marks_data})

def edit_view(request, id):
    if request.method == 'GET':
        stud = Marks.objects.get(id = id)
        form = MarksForm(instance=stud)
        return render(request, 'app1/update_stud.html', context={'form': form})
    
    elif request.method == 'POST':
        stud = Marks.objects.get(id=id)
        form = MarksForm(request.POST, instance=stud)
        if form.is_valid():
            form.save(commit=True)
            return redirect('update')    ##########
        else:
            return render(request,'app1/update_stud.html', context={'form':form})

def search_view(request):
    return render(request, 'app1/search.html')

def find_view(request):
    rollno = request.GET.get('rollno')
    try:
        stud = Marks.objects.get(rollno = rollno)
        return render(request, 'app1/search.html', context={'stud': stud})
    except:
        msg = "Invalid Roll No"
        return render(request, 'app1/search.html', context={'msg': msg})
    