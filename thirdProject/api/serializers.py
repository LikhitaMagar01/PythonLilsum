from rest_framework import serializers
from django import forms

class UsersSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    phonenumber = serializers.IntegerField()

class UsersForm(forms.Form):
    name = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    phonenumber = forms.IntegerField()