from django.urls import path
from .views import home,reg_page,addmodal,home2

urlpatterns = [
    path('', home, name='home'),
    path('signup/', reg_page, name='reg_page'),
    path('home/', home2, name='home2'),

    path('addmodal/', addmodal, name='addmodal'),

]
