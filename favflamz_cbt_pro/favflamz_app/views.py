from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import Select
from . import models
import requests
from bs4 import BeautifulSoup

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
    select = request.POST.get('search')
    print(select)


    context ={
        'search':select
    }

    return render(request, 'sub and yrs.html',context)




def instruction_page(request):
    return render(request,'instruction page.html')


def chemistry_page(request):














    return render(request, 'chemistry page.html')







