from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers

# Create your views here.
class RegistrationViewSet(viewsets.ModelViewSet):
    queryset=models.Registration.objects.all()
    serializer_class=serializers.RegistrationSerializers


