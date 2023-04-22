from .models import ReadWorker
from .serializers import ReadWorkerSerializer
from rest_framework import viewsets

class ReadOnlyWorkerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ReadWorker.objects.all()
    serializer_class = ReadWorkerSerializer


