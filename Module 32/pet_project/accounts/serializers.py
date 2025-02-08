from rest_framework import serializers
from .import models


class RegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Registration
        fields='__all__'