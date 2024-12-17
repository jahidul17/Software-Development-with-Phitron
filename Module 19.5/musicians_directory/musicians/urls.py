from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.musicians,name='musician_page')
    
]
