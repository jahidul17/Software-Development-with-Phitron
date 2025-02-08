from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset=models.Post.objects.all()
    serializer_class=serializers.PostSerializers


