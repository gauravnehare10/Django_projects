from django.shortcuts import render, redirect
from .forms import DocumentForm

# Create your views here.

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = DocumentForm()
        return render(request, 'app1/upload.html', context={'form': form})
        
def upload_success(request):
    return render(request, 'app1/upload_success.html')
