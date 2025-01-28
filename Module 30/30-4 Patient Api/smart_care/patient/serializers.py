

from rest_framework import serializers
from . import models

class PatientSerializer(serializers.ModelSerializer):
    #user name show alter user id in api list
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Patient
        fields = '__all__'