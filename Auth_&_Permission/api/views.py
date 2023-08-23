from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     #Local Authentication
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]

# class StudentModelViewSet2(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
    #Local Authentication if you want to allow anyone to view this api
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [AllowAny]

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #Local Authentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]