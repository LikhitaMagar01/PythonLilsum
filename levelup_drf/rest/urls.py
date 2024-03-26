from django.urls import path
from .views import add_two_numbers, add_two_numbers_rest

app_name = 'rest'

urlpatterns = [
    path('add/', add_two_numbers),
    path('v2/add/', add_two_numbers_rest)
]