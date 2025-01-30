

# from rest_framework.routers import DefaultRouter
# from django.urls import path, include
# from . import views
# router = DefaultRouter() # amader router

# router.register('list', views.PatientViewset) # router er antena
# urlpatterns = [
#     path('', include(router.urls)),
#     path('register/',views.UserRegistrationApiView.as_view(),name='register'),
#     path('login/',views.activate,name='login'),
#     path('active/<uid64>/<token>/',views.activate,name='activate'),
# ]

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register('list', views.PatientViewset) # router er antena
urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.UserRegistrationApiView.as_view(), name='register'),
    path('login/',views.UserLoginApiView.as_view(),name='login'),
    path('active/<uid64>/<token>/', views.activate, name = 'activate'),
]






