from rest_framework import serializers
from .models import Control

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = '__all__'
