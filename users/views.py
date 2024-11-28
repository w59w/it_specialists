
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
from .models import ITSpecialist


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.salary = request.POST.get('salary')  # Middleware уже добавил зарплату
            user.save()
            login(request, user)
            return redirect('user_list')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_list')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


@login_required
def user_list(request):
    users = ITSpecialist.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def logout_view(request):
    logout(request)
    return redirect('login')
