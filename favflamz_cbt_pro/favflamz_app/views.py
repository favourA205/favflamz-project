from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def reg_page(request):
    return render(request, 'regpage.html')