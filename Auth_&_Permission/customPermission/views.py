from .models import Worker
from .serializers import WorkerSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .customPermissions import MyPermission

class WorkerModelViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [MyPermission]