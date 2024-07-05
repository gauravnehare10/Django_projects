from django import forms

class TestForm(forms.Form):
    test_field1 = forms.BooleanField(label = 'Show Password', required=False)
    CHOICES = (
        (1, 'ONE'),
        (2, 'TWO'),
        (3, 'THREE'),
        (4, 'FOUR')
    )
    test_field2 = forms.ChoiceField(label = 'choose', choices = CHOICES)
    test_field3 = forms.DecimalField(label='Float Value', decimal_places=2)
    test_field4 = forms.EmailField(label='Email')
