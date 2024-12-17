
from django.urls import path,include
from .import views

urlpatterns = [
    #when work with cookie
    path('',views.home),
    path('get/',views.get_cookie),
    path('del/',views.delete_cookie),

]