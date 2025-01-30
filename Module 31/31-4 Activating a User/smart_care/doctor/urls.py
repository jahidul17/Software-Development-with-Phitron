from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter() # amader router

router.register('Specialization', views.SpecializationViewset) 
router.register('Designation', views.DesignationViewset) 
router.register('AvailableTime', views.AvailableTimeViewset) 
router.register('list', views.DoctorViewset) 
router.register('Review', views.ReviewViewset) 

urlpatterns = [
    path('', include(router.urls)),
]