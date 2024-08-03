from django.contrib.auth.models import User
from django import forms
class UserForm(forms.Form):
    class Meta:
        model = User
        fields = ['username', 'password']
