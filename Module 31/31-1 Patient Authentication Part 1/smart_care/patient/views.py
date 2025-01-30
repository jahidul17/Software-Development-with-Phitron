  
    
from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.views import APIView

class PatientViewset(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
    

class UserRegistrationApiView(APIView):
    serializers_class=serializers.RegisterationSerializer    
    
    
    