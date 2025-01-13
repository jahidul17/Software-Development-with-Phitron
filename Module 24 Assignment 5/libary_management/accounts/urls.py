from django.urls import path
from .views import signup,user_login,profile,user_logout,password_change,edit_profile

urlpatterns = [
    path('registation/',signup,name='registation_page'),
    path('login/',user_login,name='login_page'),    
    path('logout/',user_logout,name='logout_page'),
    path('profile/',profile,name='profile_page'),
    path('password_change/',password_change,name='password_change_page'),
    path('edit_profile/',edit_profile,name='edit_profile_page'),

]