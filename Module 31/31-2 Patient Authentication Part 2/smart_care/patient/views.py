  
    
from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

class PatientViewset(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
    

class UserRegistrationApiView(APIView):
    serializer_class=serializers.RegisterationSerializer
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data) #like form
        
        if serializer.is_valid():
            user=serializer.save()
            print(user)
            return Response("Form Done")
        return Response(serializer.errors)    
    
  
    
    