from django import forms
from django.core import validators
import re
from django.core.exceptions import ValidationError

def validate1(value):
    print("Inside Validate1")

def ifsc_validator(code):
    m = re.fullmatch(r'[A-Z]{4}\d{7}', code)
    if m == None:
        raise ValidationError("Invalid IFSC Code")
    else:
        return code
    
def upper_case(name):
    if name.isupper():
        return name
    else:
        raise ValidationError("Name must in Upper Case")
    

class TestForm(forms.Form):
    field1 = forms.CharField(label = "Field1", validators = [validate1])

class TransactionForm(forms.Form):
    accno = forms.CharField(label="Account No.")
    cname = forms.CharField(label='Customer Name', validators=[upper_case])
    ifsccode = forms.CharField(label='IFAC Code', validators=[ifsc_validator])

    