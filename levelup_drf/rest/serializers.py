from rest_framework import serializers

class AddTwoNumberSerializer(serializers.Serializer):
    number1 = serializers.IntegerField()
    number2 = serializers.IntegerField()