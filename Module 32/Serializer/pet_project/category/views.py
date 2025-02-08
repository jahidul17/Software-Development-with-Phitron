from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializer

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset=models.Categories.objects.all()
    serializer_class=serializer.CategorySerializer
    
    
