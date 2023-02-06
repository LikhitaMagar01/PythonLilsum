from rest_framework import serializers
from .models import ReadWorker

class ReadWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadWorker
        fields = ['id', 'name', 'roll', 'city']