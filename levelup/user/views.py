from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from user.forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

USER = get_user_model()

def login_view(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                print('user is found', user)
                login(request, user)
                return redirect('/user/profile/')
            else:
                print('user not found', user)
            print(form.cleaned_data)

    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/user/profile/')
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})
    
@login_required()
def profile_view(request):

    return render(request, 'user/profile.html')

def logout_view(request):

    logout(request)
    return redirect('/user/login/')

def signup_view(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print('form is valid', form.cleaned_data)
            user = USER(
                username = form.cleaned_data['username'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name']
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/user/login/')

    elif request.method == 'GET':
        form = SignUpForm()

    return render(request, 'user/signup.html', {'form': form})