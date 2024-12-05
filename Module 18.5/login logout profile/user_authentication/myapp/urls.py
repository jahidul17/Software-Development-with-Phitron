from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home_page'),
    path('profile/',views.profile, name='profile_page'),
    path('signup/',views.signup, name='signup_page'),
    path('login/',views.user_login, name='login_page'),
    path('logout/',views.user_logout, name='logout_page'),
]
