from django.shortcuts import redirect, render
from crud.models import UserInfo
from django.shortcuts import get_object_or_404
from .forms import UserInfoModelForm

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


def create_user_info(request):
    if request.method == 'POST':
        form = UserInfoModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print('form is valid')
            form.save()
            return redirect('/crud/list/')
        else:
            print('form is invalid')
    else: 
        form = UserInfoModelForm()
        # form procss
    return render(request, 'crud/create.html', {
        'form': form
    })

def update_user_info(request, user_id):
    user_object = get_object_or_404(UserInfo, id=user_id)
    if request.method == 'POST':
        form = UserInfoModelForm(request.POST, instance=user_object)
        if form.is_valid():
            print(form.cleaned_data)
            print('form is valid')
            form.save()
            return redirect(f'/detail/{user_id}')
        else:
            print('form is invalid')
    else: 
        form = UserInfoModelForm(instance=user_object)
        # form procss
    return render(request, 'crud/create.html', {
        'form': form
    })

def delete_user_info(request, user_id):
    user_object = get_object_or_404(UserInfo, id=user_id)
    user_object.delete()
    return redirect('/crud/list/')