from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.taskpage, name='taskpage'),
    path('edit/<int:task_id>',views.edit_task, name='edit_task'),
    path('delete/<int:del_id>',views.delete_task, name='delete_task'),
]