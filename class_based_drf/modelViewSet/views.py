from django.shortcuts import render
from .models import Workers
from .serializers import WorkersSerializer
from rest_framework import viewsets

class WorkerModelViewSet(viewsets.ModelViewSet):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializer
