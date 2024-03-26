from django.db import models

class Teacher(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname
    

class Student(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.IntegerField()
    teacher = models.ManyToManyField(Teacher, related_name='teachers')
    joined_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    number_of_subject = models.IntegerField(default=0)

    def __str__(self):
        return self.firstname