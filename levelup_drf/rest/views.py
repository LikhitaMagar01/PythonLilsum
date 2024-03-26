from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from .serializers import AddTwoNumberSerializer
@csrf_exempt
def add_two_numbers(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'welcome to add two number'})
    
    elif request.method == 'POST':
        print("request.post", request.POST)
        data = JSONParser().parse(request)
        print("data", data)

        serializer = AddTwoNumberSerializer(data=data)
        if serializer.is_valid():
            number1 = serializer.validated_data['number1']
            number2 = serializer.validated_data['number2']
            result = number1 + number2
            return JsonResponse({'result': result})
        print(serializer.error_messages)
        return JsonResponse({'error': 'something is missing'}, status=400)
    

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import renderer_classes

@api_view(['GET', 'POST'])
def add_two_numbers_rest(request):
    if request.method == 'GET':
        return Response({'message': 'welcome to add two number'})
    
    elif request.method == 'POST':
        serializer = AddTwoNumberSerializer(data=request.data)
        if serializer.is_valid():
            number1 = serializer.validated_data['number1']
            number2 = serializer.validated_data['number2']
            result = number1 + number2
            return Response({'result': result})
        print(serializer.errors)
        return Response(serializer.errors, status=400)