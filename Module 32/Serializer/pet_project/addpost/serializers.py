from rest_framework import serializers
from .import models


class PostSerializers(serializers.ModelSerializer):
    category = serializers.StringRelatedField( many=False)
    origin = serializers.StringRelatedField( many=False)
    class Meta:
        model=models.Post
        fields='__all__'


