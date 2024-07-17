"""
URL configuration for project38 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/', GreetView.as_view()),
    #path('details/', DetailsView.as_view()),
    path('display/<msg>/', DisplayTemplateView.as_view()),
    path('markslistview/', MarksView.as_view()),
    path('cmarkslistview/', CMarksView.as_view()),
    path('fmarksview/', FMarksView.as_view()),
    path('dmarks/<int:pk>', DMarksView.as_view())
]
