"""
URL configuration for project39 project.

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
    path('create/', ProductCreateView.as_view(), name = 'create'),
    path('home/', IndexView.as_view(), name = 'home'),
    path('update/<pk>/', ProductUpdateView.as_view(), name = 'update'),
    path('ulist/', ProductUListView.as_view(), name = 'ulist'),
    path('dlist/', ProductDeleteListView.as_view(), name = 'dlist'),
    path('delete/<pk>', ProductDeleteView.as_view(), name = 'delete'),
    path('plist/', ProductListView.as_view(), name = 'plist')
]
