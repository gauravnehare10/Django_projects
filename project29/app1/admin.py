from django.contrib import admin
from app1.models import Employees
# Register your models here.

@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    exclude = ['salary']   # while create, update, delete 
    
    list_display = ['empno', 'ename', 'salary']
    empty_value_display = '--empty--'

#admin.site.register(Employees, EmployeeAdmin)
