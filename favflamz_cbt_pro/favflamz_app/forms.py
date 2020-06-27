from django import forms
from .models import RegistrationData

class RegistrationForm(forms.ModelForm):
    class meta:
        fields = [
            'First_name',
            'Last_name',
            'Email',
            'Phone_number',

        ]
