from django import forms

class StudentForm(forms.Form):
    rollno = forms.IntegerField(label='Roll No.')
    sname = forms.CharField(label='Name', max_length=100)
    courses = forms.CharField(label='Course Name')
    fees = forms.DecimalField(label='Fees', decimal_places=2)
    remarks = forms.CharField(label='Remark', widget=forms.Textarea, max_length=200)
    