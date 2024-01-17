from django.shortcuts import render
from crud.models import UserInfo
from django.shortcuts import get_object_or_404

def list_all_user(request):
    data = UserInfo.objects.all()
    context={
        'data': data
    }
    return render(request, 'crud/list.html', context=context)

def detail_view_user(request, user_id):
    print(user_id)
    data = get_object_or_404(UserInfo, id=user_id)
    return render(request, 'crud/detail.html', context={'user_obj': data})