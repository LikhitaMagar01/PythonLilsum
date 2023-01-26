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
#     name = serializers.CharField(max_length=100)
#     city = serializers.CharField(max_length=100)
#     phonenumber = serializers.IntegerField()

# def create(self, validate_data):
#     return Student.objects.create(**validate_data)
