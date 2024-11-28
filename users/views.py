
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from .forms import RegistrationForm, LoginForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.cache import cache_page
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


@cache_page(60 * 15)
@login_required()
def user_list(request):
    users = ITSpecialist.objects.only('username', 'qualification', 'salary')
    paginator = Paginator(users, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'users/user_list.html', {'page_obj': page_obj})


def logout_view(request):
    logout(request)
    return redirect('login')
