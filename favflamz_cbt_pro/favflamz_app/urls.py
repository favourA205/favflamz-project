from django.urls import path
from .views import home, reg_page, page1, base_home,addUser

urlpatterns = [
    path('', home, name='home'),
    path('signup/', reg_page, name='reg_page'),
    path('addUser/', addUser, name='addUser'),
    path('page1/', page1, name='page1'),
    path('home/', base_home, name='base_home'),


]
