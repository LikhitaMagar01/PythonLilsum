from django.urls import path
from .views import FirstView, FirstTemplate
from .crud_views import Create, List, Detail, Update, Delete

app_name = 'classbased'

urlpatterns = [
    path('first/', FirstView.as_view()),
    path('template/', FirstTemplate.as_view()),
    path('template/2', FirstTemplate.as_view()),
    path('template/3', FirstTemplate.as_view()),
    path('template/4', FirstTemplate.as_view()),
    
    path('create/', Create.as_view(), name='create'),
    path('list/', List.as_view(), name='list'),
    path('detail/<int:id>/', Detail.as_view(), name='detail'),
    path('update/<int:id>/', Update.as_view(), name='update'),
    path('delete/<int:pk>/', Delete.as_view(), name='delete')
]