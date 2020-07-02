from django.shortcuts import render,redirect
from .forms import RegistrationForm


# Create your views here.
def home(request):
    return render(request, 'base.html')

def reg_page(request):
    context = {
        'form':RegistrationForm
    }

    return render(request, 'regpage.html',context)

def addUser(request):
    register = RegistrationForm(request.POST)

    if register.is_valid():
        register.save()

    return redirect('base_home')

def page1(request):
    return render(request, 'sub and yrs.html')

def base_home(request):
    return render(request,'base home.html')










