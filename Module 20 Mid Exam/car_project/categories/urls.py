from django.urls import path,include
from .import views


urlpatterns = [
    path('brand/',views.add_brand, name='add_brand')
]