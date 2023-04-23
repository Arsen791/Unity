from django.shortcuts import render, redirect
from user.forms import UserRegistrationForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import login, logout

# Create your views here.
def login_page(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.data.get('username')
            password = form.data.get('password')
            user = auth.authenticate(username=username, password=password)
            if username == 'AlmaU' and password == 'alma2023':
                return redirect('/all.html')
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'user/login.html', {'form': form})


def register_page(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
        return render(request, 'user/registration.html', {'form': form})
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            password = form.data.get('password')
            status = form.data.get('status')
            auth_data = auth.authenticate(request, email=user.email, password=password, status=status)
            login(request, user)
            if auth_data is not None:
                return redirect('/')
            return redirect('/auth/login/')
        else:
            return render(request, 'user/registration.html', {'form':form})
        
def logout_page(request):
    logout(request)
    return redirect('/auth/login/')