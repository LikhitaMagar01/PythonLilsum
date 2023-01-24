from django.shortcuts import render
from .models import Users
from .serializers import UsersSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.

#model object - single user data
# def user_detail(request, pk):
#     stu = Users.objects.get(id=pk)
#     serializer = UsersSerializer(stu)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type = 'application/json')

#model object - single user data - using JSONResponse
def user_detail(request, pk):
    stu = Users.objects.get(id=pk)
    serializer = UsersSerializer(stu)
    return JsonResponse(serializer.data)

#Query Set - all data
def user_list(request):
    stu = Users.objects.all()
    serializer = UsersSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = 'application/json')

#Query Set - all data - using JsonResponse
#it is no-dict that's why safe=False
def user_list(request):
    stu = Users.objects.all()
    serializer = UsersSerializer(stu, many=True)
    return JsonResponse(serializer.data, safe=False)