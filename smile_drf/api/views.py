from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Gamer
from .serializers import GamerSerializer
from rest_framework import status, serializers
  
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by username': '/?username=username',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
  
    return Response(api_urls)

@api_view(['POST'])
def add_items(request):
    item = GamerSerializer(data=request.data)
  
    # validating for already existing data
    if Gamer.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)