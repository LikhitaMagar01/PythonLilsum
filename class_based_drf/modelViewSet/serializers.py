from rest_framework import serializers
from .models import Workers

class WorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = ['id', 'name', 'roll', 'city']