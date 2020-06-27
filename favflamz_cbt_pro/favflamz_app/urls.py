from django.urls import path
from .views import home,reg_page

urlpatterns = [
    path('', home, name='home'),
    path('signup/', reg_page, name='reg_page'),
]
