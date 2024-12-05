from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name='home_page'),
    path('profile/',views.profile, name='profile_page'),
    path('signup/',views.signup, name='signup_page'),
    path('login/',views.user_login, name='login_page'),
    path('logout/',views.user_logout, name='logout_page'),
    path('change_password/',views.password_change, name='ChangePass_page'),
    path('change_password_withoutOldpass/',views.pass_change_withoutOldpass, name='ChangePass_withoutOldpass_page'),
    path('edit_profile/',views.edit_profile, name='edit_profile_page'),
]
