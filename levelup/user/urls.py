from django.urls import path
from user.views import (login_view, profile_view, logout_view, signup_view)
app_name = 'user'
urlpatterns = [
    #{% url 'crud:list' %}
    path('profile/', profile_view, name='profile'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup')
]