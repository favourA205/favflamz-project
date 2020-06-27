from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import RegistrationData
# Create your views here.
def home(request):
    return render(request, 'base.html')

def reg_page(request):

    my_data = {
        "form": RegistrationForm

    }
    return render(request, 'regpage.html', my_data)

