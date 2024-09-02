from django.urls import path
from app1.views import *

urlpatterns = [
    path('upload_file', upload_file, name='upload_file'),
    path('upload_success/', upload_success, name='upload_success')
]