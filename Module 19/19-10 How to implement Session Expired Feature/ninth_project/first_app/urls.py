
from django.urls import path,include
from .import views

urlpatterns = [
    #when work with cookie
    # path('',views.home),
    # path('get/',views.get_cookie),
    # path('del/',views.delete_cookie),
    
    
    #when work with session
    path('',views.set_session),
    path('get/',views.get_session),    
    # path('del/',views.delete_session),
]