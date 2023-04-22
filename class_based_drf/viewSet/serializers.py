from rest_framework import serializers
from .models import Family

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ['id', 'name', 'roll', 'city']