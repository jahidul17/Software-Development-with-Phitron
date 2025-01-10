from django.urls import path,include
from .views import UserRegistrationView,UserLoginView,UserBankAccountUpdateView
from .import views

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    # path('logout/',UserLogoutView.as_view(),name='logout'), #i don't know why is not work.
    path('logout/',views.user_logout,name='logout'),
    path('profile',UserBankAccountUpdateView.as_view(),name='profile')# profile page is not clear
    
]
