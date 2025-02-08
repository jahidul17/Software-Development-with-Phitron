from rest_framework import serializers
from .import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Categories
        fields='__all__'
        


