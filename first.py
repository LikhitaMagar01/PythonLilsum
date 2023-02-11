print("hello")

# using correct datatype is necessary for effeciency, security and retening a meaning
# python:
# List
getList = ["quill", "wheel", "eraser", "referee", "trouser"]
# print(getList)
# -- use to store multiple items in a single variable
# -- one of the built-in data types 
# -- store collections of data
# -- use square bracket
# -- create ordered, changable list and allow duplicates
# to determine lenght of list: len()
# print(len(getList))
# to determine type of list: type
# print(type(getList))

# list() constructor
getList = list(("quill", "wheel", "eraser", "referee", "trouser"))
# print(getList)

# access items
# you can access list item by its index number
# first item is index 0 last item is -1
# print(getList[3])

# range of index
# starts from 1 and end in 2 index; 3 is not included
# [:2] means first to 2; [2:] means 2 index to last
# print(getList[1:3])
# print(getList[-5:-2])
# check item in list
getList = ["quill", "wheel", "eraser", "referee", "trouser"]
if 'eraser' in getList:
    print('yippe! it is there')
# change item value
getList[3]= "rose water"
# print(getList[3])

# change item in range
getList[1:3]=["worried", "error"]
# print(getList[1:3])

# insert item acc to index
getList.insert(1, "quiet")
# print(getList)

# add item
getList.append("young")
# print(getList)

# add list to list or tuple or set or dictionaries
addList=["hi", "namaste", "ohayo", 1]
getList.extend(addList)
# print(getList)

# remove 
# remove specific item
# getList.remove("quiet")
# print(getList)

# remove specific index
getList.pop(5)
# print(getList)

del getList[6]
# print(getList)

# remove last item
getList.pop()
# print(getList)

# clear list 
# clear item; keeps list
print(addList)
addList.clear()
# print(addList)

# loop in list
# for x in getList:
#     print(x)

# loop using index
# for i in range(len(getList)):
    # print(getList[i])

# while loop 
i = 1
while i < len(getList):
    print(getList[i])
    i = i+1

# sort list alphabetically
# case sensitive; priority to uppercase than lowecase
getList.sort()
print(getList)
getList.sort(reverse=True)
print(getList)
def func(n):
    return abs(n - 2)

numlist= [1,2,3,4,5,6,7]
numlist.sort(key=func)
# print(numlist)
thislist = ["quill", "Wheel", "Eraser", "Referee", "trouser"]
thislist.sort(key = str.lower)
# print(thislist)
thislist.reverse()
print(thislist)

# copy list
copyList = getList.copy()
print("copy list", copyList)

# set
# --unchangeable but can remove or add items as you want

# dictionaries
# -- ordered items

# one liner
onelist = ["quill", "wheel", "eraser", "referee", "trouser"]
# otherlist = [x for x in onelist if "e" in x]
# print(otherlist)
# variable = [expression for item in iterable if condition == true]
# otherlist = [x for x in onelist if x == "eraser"]
# print("it is use to erase")

# API:
# Application Programming Interface
# it is language independent concept.
# Software inter-mediator to communicate between applications
# can be use by web application, andriod, java or python application to interact with same database
# types in terms of release policy:
# Private API
# private application from a company
# business partner
# can be share to partners
# public 
# can be use by third party developers

# REST API:
# architectural guideline to make api 
# client makes HTTP requests to API
# api communicate to web application/database 
# provides data to api
# return data to api

# CRUD operations:
# operation: create, read, update, delete
# http methods: POST, GET, PUT/PATCH, DELETE
# description: create/post/inserting data  reading/geting data  update single-patch update all – put delete data

# api example:
# http://geekyshows.com/api/students

# geekyshows.com- Base URL
# api- naming convention
# students- resource of API or endpoint

# post: api/students, data
# get:  api/students
#        api/students/id
# put: api/students/id, data
# patch: api/students/id, data
# delete: api/students/id

# serializer and serializer class:
# python JSON:
# python has a built-in package called json, which is used to work with json data
# types of methods:
# dumps(data)- convert python object into json string
# example:
# python_data = {‘name’: ‘sonam’, ‘roll’: 101}
# json_data = json.dumps(python_data)
# print(json_data)
# {“name”: “sonam”, “roll”: 101}
# difference is: single inverted and double inverted comma

# loads(data)- use to parse json string
# example: 
# import json
# json_data = json.dumps(python_data)
# parsed_data = json.loads(json_data)
# print(parse_data)
# {‘name’: ‘Sonam’, ‘roll’: 10}

# serializers:
# responsible for converting complex data such as querysets and model instances to native python datatypes which can be rendered into json, xml or other content types
# responsible for deserialization; parse data to be converted into complex types after validating the incoming data

# *serializer
# *deserializer

# Django Form and ModelForm class 

# DRF uses serializer class.
# Create separate serializers.py to write all serializers
# from rest_framework import serializers
# class StudentSerializer(serializers.Serializer):
#          name= serializers.IntegerField()
#          roll= serializers.IntegerField()
#          city= serializers.CharField(max_length=100)



# complex data type into python native data type using serializer into json 

# create model object stu
# stu = Student.objects.get(id=1)

# converting model instance stu to python Dict/ serializing object
# serializer = StudentSerializer(stu)

# create query set
# stu = Student.objects.all()

# converting Query Set stu to List of Python Dict/ Serializing Query Set
# serializer = StudentSerializer(stu, many=True)
# print(serializer.data)

# JSON Renderer:
# convert serialized data into JSON
# import JSONRenderer
# from rest_framework.renderers import JSONRenderer

# Render the Data into Json
# json_data = JSONRender().render(serializer.data)

# JsonResponse()
# subclass to httpresponse
# JsonResponse(data, encoder=DjangoJSONEncoder, safe=True, json_dumps_params=None, **kwargs)

# Serializer Class:
# class UsersSerializer(serializers.Serializer):
# name = serializers.CharField(max_length=100)
# city = serializers.CharField(max_length=100)
# phonenumber = serializers.IntegerField()

# serializer field converts between primitive values and internal datatype.
# Deals with validating input values, retrieving and setting the values from their parent objects.

# CharField: text representation, validation or max_length and min_length
# CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
# max_length = no more no. of character
# min_length = no less no. of character
# allow_blank = default= False, set True if empty string should be considered a valid value.
# trim_whitespace = default = False, set True if leading and trailing white-space is trimmed
# allow_null = available for string field, also its usage is discouraged in favor of allow_blank

# IntegerField: integer representation
# IntegerField(max_value=None, min_value=None)
# max_value = > value
# min_value = < value

# FloatField: integer representation
# FloatField(max_value=None, min_value=None)
# max_value = > value
# min_value = < value

# DecimalField = a decimal representation
# DecimalField(max_digits, decimal_place, coerce_to_string=None, max_value=None, min_value = None)
# max_digits = max number of digits allowed in number
# decimal_places = number of decimal places to store with the number
# coerce_to_string = default = False, set true if string value should be return for the representation
# setting localize will force the value to True
# max_value Validate > value
# min_value validate < value


# SlugField: RegexField that validates the input against the pattern
# SlugField(max_length=50, min_length=None, allow_blank=False)

# EmailField(max_length=50, min_length=None, allow_blank=False)

# BooleanField()

# NullBooleanField: accepts boolean value also null as a valid value
# NullBooleanField()

# URLField – url pattern http:
# URLField(max_length=50, min_length=None, allow_blank=False)

# FileField – file representation
# FileField(max_length=None, allow_empty_file=false, use_url=UPLOADED_FILES_USE_URL)
# max_length - maximum length of file name
# allow_empty_file - empty files are allowed
# use_url - defaults to true, if set false then filename string values will be used for the output representation

# ImageField - An image representation
# ImageField(max_length=None, allow_empty_file=false, use_url=UPLOADED_FILES_USE_URL)

# TimeField - time representation
#TimeField(format=api_settings.TIME_FORMAT, input_formats=None)

# DateTimeField 
# DateTimeField(format=api_settings.DATETIME_FORMAT, input_formats=None, default_timezone=None)

# DurationField
# DurationField(max_value=None, min_value=None)

# RegexField(regex, max_length=None, min_length=None, allow_blank=False)

#UUIDField(format='hex_verbose')

# FilePathField

# ChoiceField(choices)

# De-serialization
# parded data to be converted into complex types after validating the incoming data

# complex_data_type ---serialization---> python native data type ---render into json---> json data

# into

# json data ---parse data---> python native data type ---de-serialization---> complex data type

# for this 
# to converted json data into parsed data

# BytesIO()
# strem implementation using an in-memory bytes buffer
# import io
# stream = io.BytesIO(json_data)

# JSONParser()
# parse json data to python native data type
# from rest_framework.parsers import JSONParser
# parsed_data = JSONParser().parse(stream)

# now the parsed data is converted into complex data by de-serialization

# create serializer object
# serializer = StudentSerializer(data = parsed_data)

# Validated Data
# serializer.is_valid()

# serializer.validated_data
# setializer.errors

# de-serialization is done when client gives json value from front-end
# from rest_framework import serializers
# class StudentSerializer(serializers.Serializer):
# name = serializers.CharField(max_length=100)
# city = serializers.CharField(max_length=100)
# phonenumber = serializers.IntegerField()

# def create(self, validate_data):
# return Student.objects.create(**validate_data)

# Better way to create Django Project:
# virtual environment:
# in multiple project you need multiple virtual environment which helps in creating self-consistent and independent unit spaces on your system.

# Install venv module to create virtual environment
# sudo apt-get install -y python3-venv

# now open a folder in you vs code or other text editor and in terminal:
# python3 -m venv virtualEnv

# this creates a folder of virtualEnv which will contains objects which are helping your to create a virtual environment

# now, to activate the virtual environment:
# source virtualEnv/bin/activate

# install Django using pip:
# python3 -m pip install Django

# check django admin version:
# django-admin –version

# create a django project:
# django-admin startproject myHome

# pip freeze to see drf version

# now create an app:
# app is a web application that has specific meaning in the project like homepage, aboutpage, or members databases

# python3 manage.py startapp family

# migrate :
# python3 manage.py makemigrations
# python3 manage.py migrate

# GenericAPIView

# attributes

# queryset- should be used for returning objects from this view.
#           either set this attributes or override get_queryset() instead of accessing this property directly.
#           queryset will be evaluated once and those results are cached for all subsequent requests.

# serializer_class- The serializer class that should be sued for validating and deserializing input and for serializing output. 
#                   either set this attribute or override the get_serializer_class() method.

# lookup_field- should be used for performing object lookup of individual model instances.
#               it is default to pk

# lookup_url_kwarg- the URL keyword argument that should be used for object lookup.
#                   the URL conf should include a keyword argument corresponding to this value. If unset this defaults to using the same value as lookup_field.

#pagination_class- pagination class should be used when paginating list results. 
#                  defaults to same value as the DEFAULT_PAGINATION_CLASS setting, this is 'rest_framework.pagination.PageNumberPagination'.Settingpagination_class=None will be disable pagination on this view.

# methods:
# get_queryset(self)
# returns queryset which is used for list views, and that should be used as the base for lookups in detail views. 
# detault to returning the queryset specified by the queryset attribute.

# get_object(self): 
# it return an object instance that should be used for detail views. detaults to using the lookup_field parameter to filter the base queryset.

# get_serializer_class(self):
# returns the class that should be used for the serializer. defaults to returning the serializer_class attribute.

# get_serializer_context(self):
# returns a dictionary containing any extra context that should be supplied to the serializer. detaults to including 'request', 'view', and 'format' keys.

# get_serializer(self, instance=None, many=False, partial= False)
# it returns a serializer instance

# get_paginated_response(self, data)
# it returns a serializer instance

# paginate_queryset(self, queryset)
# paginate a queryset if required, either returning a page object or None if pagination is not configured for this view.

# filter_queryset(self, queryset)
# give a queryset, filter it with whichever filter backends are in use, returning a new queryset.

# mixins
# common behavior CRUD are implemented provided by mixin classes
# ListModelMixin
# CreateModelMixin
# RetrieveModelMixin
# UpdateModelMixin
# DestroyModelMixin

# ListModelMixin
# provides a list(request, *args, **kwargs) methods that implements listing a queryset.
# if the queryset is populated, returns 200 OK response, with a serialized representation of the queryset as the response.
# from rest_framework.mixins import ListModelMixin
# from rest_framework.generics import GenericAPIView
# class StudentList(ListModelMixin, GenericAPIView):
#   queryset = Student.objects.all()
#   serializer_class = StudentSerializer
#   def get(self, request, *args, **kwargs):
#      return self.list(request, *args, **kwargs)

# CreateModelMixin
# provides a create(request, *args, **kwargs) method
# implements creating and saving a new model instance
# if an object creates return 201 resonse with serialized representation contains a key named url, then location header of the response will be populated with that value.
# else 400 bad request response will be returned with the error details as the body of the response
# from rest_framework.mixins import CreateModelMixin
# from rest_framework.generics import GenericAPIView
# class StudentCreate(CreateModelMixin, GenericAPIView):
#   queryset = Student.objects.all()
#   serializer_class = StudentSerializer
#   def post(self, request, *args, **kwargs):
#      return self.create(request, *args, **kwargs)

# RetrieveModelMixin
# provides a retrieve(request, *args, **kwargs) method
# if an object is retrieve, return 20 resonse with serialized representation of the object as the body of the response
# else 404 bad request response will be returned with the error details as the body of the response
# from rest_framework.mixins import RetrieveModelMixin
# from rest_framework.generics import GenericAPIView
# class StudentCreate(RetrieveModelMixin, GenericAPIView):
#   queryset = Student.objects.all()
#   serializer_class = StudentSerializer
#   def post(self, request, *args, **kwargs):
#      return self.retrieve(request, *args, **kwargs)

# UpdateModelMixin
# provides a update(request, *args, **kwargs) method
# provides partial_update(request, *args, **kwargs)
# if an object is update, return 20 resonse with serialized representation of the object as the body of the response
# else 400 bad request response will be returned with the error details as the body of the response
# from rest_framework.mixins import UpdateModelMixin
# from rest_framework.generics import GenericAPIView
# class StudentCreate(UpdateModelMixin, GenericAPIView):
#   queryset = Student.objects.all()
#   serializer_class = StudentSerializer
#   def post(self, request, *args, **kwargs):
#      return self.update(request, *args, **kwargs)

# DestroyModelMixin
# provides a destroy(request, *args, **kwargs) method
# if an object is destoy, return 204 No content response,
# else 404 bad request response will be returned with the error details as the body of the response
# from rest_framework.mixins import UpdateModelMixin
# from rest_framework.generics import GenericAPIView
# class StudentCreate(DestroyModelMixin, GenericAPIView):
#   queryset = Student.objects.all()
#   serializer_class = StudentSerializer
#   def post(self, request, *args, **kwargs):
#      return self.destroy(request, *args, **kwargs)

# Concrete View class
# ListAPIView- use for read-only endpoints to represent a collection of model instances
#              provide get handler
#              extends of GenericAPIView, ListModelMixin

# from rest_framework.generics import ListAPIView
# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# CreateAPIView
# create only endpoints
# provides a post method handler
#              extends of GenericAPIView, CreateModelMixin

# from rest_framework.generics import CreateAPIView
# class StudentCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# RetrieveAPIView
# read only endpoints
# provides a get method handler
#              extends of GenericAPIView, RetrieveModelMixin

# from rest_framework.generics import RetrieveAPIView
# class StudentRetrieve(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# UpdateAPIView
# update only endpoints
# provides a put and patch method handler
#              extends of GenericAPIView, UpdateAPIView

# from rest_framework.generics import UpdateAPIView
# class StudentUpdate(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# DestroyAPIView
# delete only endpoints
# provides a delete method handler
#              extends of GenericAPIView, DestroyAPIView

# from rest_framework.generics import DestroyAPIView
# class StudentDelete(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# ListCreateAPIView
# RetrieveUpdateAPIView
# RetrieveUpdateDestroyAPIView

# ViewSet
# allows to combine the logic for a set of related views in a single class, called viewset
# advantages
# repeated logic can be combined into a single class
# no longer need to deal with writing URL conf ourselves

# ViewSet Class
# type of class-based view
# no get() or post()
# yess list(), retrieve(), create(), update(), partial_update() and destroy()

# attributes
# basename- the base to use for the URL names that are created
# action- name of current action
# detail- boolean indicating if the current action is configured for a list or detail view
# suffix- the display suffix for the viewset type- mirrors the detail attribute
# name- the display name for the viewset. argument is manually exclusive to suffix
# description- the display description for the individual view of a viewset

# ViewSet- URL Config
# from django.urls import path, include
# from api import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('studentapi', views.StudentViewSet, basename='student')

# urlpatterns=[
#     path('', include(router.urls)),
# ]

# ModelViewSet class
# inherits from GenericAPIView
# implements various action - create, update, partial_update, and destroy.
# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# ReadOnlyModelViewSet Class
# inherits from GenericAPIView
# includes action - list() and retrieve()
# use any standard attributes and method overrides available to GenericAPIView

# class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# end
# yolo- you only live for once

############################

# Validation
# types

# Field Level Validation
# specify custom field-level validation by adding validate_fieldName methods to your Serializer subclass
# syntax: def validate_fieldname(self, value)
# example: def validate_roll (self, value)
# value is the field value that requires validation
# class StudentSerializer(serializers.Serializer):
# name = serializers.CharField(max_length=100)
# roll = serializers.IntegerField()
# city = serializers.CharFIeld(max_length=100)
# def validate_roll(self, value):
# if value >=200:
#     raise serializers.ValidationError('seat full')
# return value

# Object Level Validation
# validation that requires access to multiple fields 
# called validate() to Serializer subclass
# raise serializers.ValidationError or just return validated values
# syntax: def validate(self, data)
# example: def validate(self, data)
# where data is a dictionary of field values
# class StudentSerializer(serializers.Serializer):
# name = serializers.CharField(max_length=100)
# roll = serializers.IntegerField()
# city = serializers.CharFIeld(max_length=100)
# def validate(self, data):
#     mm = data.get('name')
#     ct = data.get('city')
#     if mm.lower()==='rohit' and ct.lower()!='rachi':
#         raise serializers.ValidationError('city must be rachi')
#     return data

# Validators
# introduce a proper separation of concerns, making your code behavior more obvious
# from rest_framework import serializers
# def starts_with_r(value):
#     if value[0].lower()!='r':
#         raise serializers.ValidationError('Name should start with R')
#     class StudentSerializer(serializers.Serializer):
#         name = serializers.CharField(max_length=100, validators=[starts_with_r])
#         roll = serializers.IntegerField()
#         city = serializers.CharField(max_lenght=100)

#################################################

# Authentication and Permission
# first of, no restriction on our api to use it
# implement authentication and permission in your api to always associate with a creator
# authenticated users may create data
# only the creator of a data may updte or delete it
# unauthenticated requests should have a full read-only access

# Authentication
# mechanism of associating an incoming request with a set of identifying credential
# permission and throttling policies can then use those credential to determine if the request should be permitted

# authentication is always run at the very start
# then permission and throttling is checked 

# types
# BasicAuthentication
# SessionAuthentication
# TokenAuthentication
# RemoteUserAuthentication
# CustomAuthentication

# Basic Authentication
# uses HTTP basic authentication, needed user name and password
# appropriate for testing only
# if authenticated, request.user will be a Django User instance
# request.auth will be None

# authenticated responses that are denied permission will result in HTTP 401 Unauthorized response with an appropriate WWW-authenticate header
# www-authenticate: Basic realm='api'

# if you are using in production, ensure your api is only available over https
# your api client will always request the user and password at login and will bever store those details to persistent storage

# Permission
# grant or deny access for different classes users to different parts of the API
# use authentication information in the request.user and request.auth properties to determine if the incoming request should be permitted

# in rest_framework, 
# permission are defined as a list permission classes
#  AllowAny
#  IsAuthenticated
#  IsAdminUser
#  IsAuthenticatedOrReadOnly
#  DjangoModelPermissions
#  DjangoModelPermissionOrAnonReadOnly
#  DjangoObjectPermissions
#  CustomPermission

# AllowAny
# allow permission whether authenticated or anauthenticated

# IsAuthenticated
# will deny permission to any anauthenticated user 
# only be accessible to registered user

# IsAdminUser
# permission allowed to user.is_staff is True 

# IsAuthenticatedOrReadOnly
# allow authenticated users to perform any request
# use if you want to allow to read permissions to anonymous users and only allow write permissions to authenticated users

# DjangoModelPermissions
# ties into Django's standard django.contrib.auth model permission
# must be applied to views that have a queryset property set
# authorization will be granted if the user is authenticated and relevant model permission is assigned
# post request require add permission on the model
# put and patch request require the user to have the change permission on the model
# delete request require the user to have delete permission on the model
# get request to view the data of the model
# can be overridden the default behaviour DjangoModelPermissions

# DjangoModelPermissionsOrAnonReadOnly
# unauthenticated users can read-only access to the api

# DjangoObjectPermissions
# allows per-object permissions on models
# need to add a permission backend that supports object-level permissions such as django-guardian

# SessionAuthentication
# uses django's default session backend for authentication
# appropriate for AJAX client that are running in the same session content as your website
# if sucessfull, provides crediential
# if not permission is denied in http 403 forbidden response
# request.user will be a django user isinstance
# request.auth will be None

# AJAX api with sessionAUthentication, you should include CSRF token for 'unsafe' http method call like post, put, patch, delete and retrieve

# Custom Permission
# overide BasePermission and implement either or both of the following methods
# has_permission(self, request, view)
# has_permission(self, request, view, obj)
# methods should return True if the request should be granted acces else False to deny access

# TokenAuthentication
# uses simple token-based HTTP authentication scheme
# configure the authentication classes to include TokenAuthentication
# include rest_framework.authtoken in your INSTALLED_APPS settings
# run migration 

# if successful, TokenAuthentication provides following credential
# request.user will be a Django User instance 
# request.auth will be a rest_framework.authtoken.models.Token instance

# if unsuccessful,
# HTTP 401 unauthorized response with an appropriate WWW-authenticate header
# example:
# WWW-Authenticate: Token

# Generate Token
# using Admin Application
# using Django manage.py command using command: 
#       python manage.py drf_create_token<username>- this command return api token for the given user or creates a token if token does not exist for user
# by exposing an API endpoint
# : you can provide a mechanism for client to obtain a token given the username and password
# from rest_framework.authtoken.views import obtain_auth_token
# urlpatterns = [
#     path('gettoken/', obtain_auth_token)
# ]
# obtain_auth_token view will return a json response when valid username and password fields are posted to the views vuing form data or json
# pip install httpie
# http POST http://127.0.0.1:8000/gettoken username='name' password='pass'
# {'token': 4567898765dfgn876dfgh}
# using Signals

# httpie
# provides command line HTTP client
# makes cli human-friendly
# syntax: http [flags][METHOD]URL[ITEM[ITEM]]
# use httpie
# get request:
# http http://127.0.0.1:8000/stutendapi/
# get request with auth:
# http http://127.0.0.1:8000/stutendapi/'Authorization:Token3456543fghvcdfgh3456'
# post request/ submitting form
# http -f POST http://127.0.0.1:8000/stutendapi/ name='jay' roll=45 city='dfg' 'Authorization:Token345654efghtr456543erfg'
# put request
# http PUT http://127.0.0.1:8000/stutendapi/ name='jay' roll=45 city='dfg' 'Authorization:Token345654efghtr456543erfg'
# delete request
# http DELETE http://127.0.0.1:8000/stutendapi 'Authorization:Token345654efghtr456543erfg'