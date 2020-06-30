from django.urls import path
from .views import home,reg_page,addmodal,page1

urlpatterns = [
    path('', home, name='home'),
    path('signup/', reg_page, name='reg_page'),
    path('page1/', page1, name='page1'),

    path('addmodal/', addmodal, name='addmodal'),

]
