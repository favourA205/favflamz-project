from django import forms
from .models import RegistrationData

class RegistrationModal(forms.ModelForm):

    class Meta:
        model = RegistrationData
        fields = [
            'First_name',
            'Last_name',
            'Email',
            'Phone_number',

        ]

    widget = [
        'First_Name'

    ]