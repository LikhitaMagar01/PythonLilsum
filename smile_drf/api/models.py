from django.db import models
  
class Gamer(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
  
    def __str__(self) -> str:
        return self.email