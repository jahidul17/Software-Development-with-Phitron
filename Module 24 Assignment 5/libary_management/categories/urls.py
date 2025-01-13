from django.urls import path,include
from .import views


urlpatterns = [
    path('categori/',views.add_categori, name='add_categori')
]


