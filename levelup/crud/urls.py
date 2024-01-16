from django.urls import path
from crud.views import list_all_user, detail_view_user

urlpatterns = [
    path('list/', list_all_user),
    path('detail/<int:user_id>/', detail_view_user)
]