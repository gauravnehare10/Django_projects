from django.urls import path
from . import views

urlpatterns = [
    path('stud_adm/', views.stud_adm),
    path('stud_info/', views.stud_info)
]