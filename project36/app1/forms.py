from django import forms
from app1.models import Employee
from django.core.exceptions import ValidationError
class EmployeeForm(forms.ModelForm):
    '''
    # Job Validation 

    def clean_job(self):
        if self.cleaned_data["job"] not in ["hr", "manager"]:
            raise ValidationError("Invalid Job")
        return self.cleaned_data["job"]
    '''
    class Meta:
        model = Employee
        fields = "__all__"