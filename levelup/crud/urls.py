from django.urls import path
from crud.views import (list_all_user, detail_view_user, 
                        create_user_info, update_user_info, 
                        delete_user_info
                        )
app_name = 'crud'
urlpatterns = [
    #{% url 'crud:list' %}
    path('list/', list_all_user, name='list'),
    path('detail/<int:user_id>/', detail_view_user, name='detail'),
    path('create/', create_user_info, name='create'),
    path('update/<int:user_id>', update_user_info, name='update'),
    path('delete/<int:user_id>', delete_user_info, name='delete')
]