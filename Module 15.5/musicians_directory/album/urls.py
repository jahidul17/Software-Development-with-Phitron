from django.urls import path,include
from .import views

urlpatterns = [
    path('add/',views.add_album, name="add_album"),
    path('edit/<int:albumID>',views.edit_album, name="edit_album"),
    path('delete/<int:albumID>',views.delete_album, name="delete_album"),
]