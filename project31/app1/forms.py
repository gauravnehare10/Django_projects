from django import forms

class LoginForm(forms.Form):
    user = forms.CharField(label='Username', max_length='20', empty_value='empty')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
