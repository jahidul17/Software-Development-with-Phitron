from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.albums,name='album_page')
    
]
