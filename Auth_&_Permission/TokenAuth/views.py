from .models import Worker
from .serializers import WorkerSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class WorkerModelViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]