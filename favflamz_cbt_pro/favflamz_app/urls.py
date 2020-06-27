from django.urls import path
from .views import home,reg_page

urlpatterns = [
    path('', home, name='home'),
    path('sign/', reg_page, name='reg_page')

]
