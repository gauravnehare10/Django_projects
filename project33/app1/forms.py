from typing import Any
from django import forms
from django.core.exceptions import ValidationError
class StudentForm(forms.Form):
    rollno = forms.IntegerField(label='Roll No.')
    sname = forms.CharField(label='Name', max_length=100)
    course = forms.CharField(label='Course Name')
    fees = forms.DecimalField(label='Fees', decimal_places=2)
    remark = forms.CharField(label='Remark', widget=forms.Textarea, max_length=200)
    
    def clean_rollno(self):
        rno = self.cleaned_data['rollno']
        if rno > 100:
            raise ValidationError("Invalid Roll No. or Roll No. must be less than 100")
        return rno
    def clean_course(self):
        crs = self.cleaned_data['course']
        if crs not in ["python", "java"]:
            raise ValidationError("Course must be python or java")
        return crs
    
    