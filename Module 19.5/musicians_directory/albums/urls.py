from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.albums,name='album_page'),
    path('edit/<int:albumID>',views.edit_album, name="edit_album"),
    path('delete/<int:albumID>',views.delete_album, name="delete_album"),
    
]
