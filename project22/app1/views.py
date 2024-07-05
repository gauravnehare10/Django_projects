from django.shortcuts import render

# Create your views here.
def display_index(request):
    return render(request, "app1/index.html")


def info_view(request, course):
    match course:
        case 'python':
            desc = '''Python is general purpose programming 
            language, This language is used for various types 
            of applications.'''
            data = {'sesc':desc, 'course':course}
            return render(request, 'app1/info.html', context=data)
        