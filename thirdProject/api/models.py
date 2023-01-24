from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phonenumber = models.IntegerField()
