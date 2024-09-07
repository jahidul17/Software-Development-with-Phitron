
from django.urls import path

from .import views

urlpatterns = [   
    path("",views.home_first_app),  
    path("course/",views.course),    
    path("about/",views.about),    
]
