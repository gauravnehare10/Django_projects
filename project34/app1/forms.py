from django import forms
from django.core import validators

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", validators=[validators.MaxLengthValidator(20), validators.MinLengthValidator(4)])
    contactid = forms.IntegerField(label="Contact ID", validators=[validators.MaxValueValidator(100), validators.MinValueValidator(1)])
    email = forms.CharField(label="Email", validators=[validators.EmailValidator])
    message = forms.CharField(label="Message", widget=forms.Textarea, validators=[validators.MaxLengthValidator(100), validators.MinLengthValidator(10)])

