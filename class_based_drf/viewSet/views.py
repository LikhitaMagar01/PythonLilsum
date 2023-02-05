from django.shortcuts import render
from rest_framework.response import Response
from .models import Family
from .serializers import FamilySerializer
from rest_framework import status
from rest_framework import viewsets
# Create your views here.

class FamilyViewSet(viewsets.ViewSet):
    def list(self, request):
        print("*****LIST****** attributes")
        print('Action', self.basename)
        print('Detail', self.action)
        print('Suffix', self.suffix)
        print('Name', self.name)
        print('Description', self.description)
        fam = Family.objects.all()
        serializer = FamilySerializer(fam, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            fam = Family.objects.get(id=id)
            serializer = FamilySerializer(fam)
            return Response(serializer.data)

    def create(self, request):
        serializer = FamilySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        id = pk
        fam = Family.objects.get(pk=id)
        serializer = FamilySerializer(fam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        id = pk
        fam = Family.objects.get(pk=id)
        serializer = FamilySerializer(fam, data=request.data,  partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'partial Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id = pk
        fam = Family.objects.get(pk=id)
        fam = Family.objects.get(pk=id)
        fam.delete()
        return Response({'msg': 'Data Deleted'})