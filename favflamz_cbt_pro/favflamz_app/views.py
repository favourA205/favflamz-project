from django.shortcuts import render,redirect
from .forms import RegistrationModal
from .models import RegistrationData
# Create your views here.
def home(request):
    return render(request, 'base.html')

def home2(request):
    return render(request, 'home.html')

def reg_page(request):
    mydata = {
        'modalforms':RegistrationModal
    }

    return render(request, 'regpage.html')

def addmodal(request):
    mymodal = RegistrationModal(request.POST)

    if mymodal.is_valid():

        mymodal.save()

    return redirect('home')









