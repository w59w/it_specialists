from django.urls import path, include
from django.shortcuts import redirect
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('users.urls')),
    path('login/', include('users.urls')),
    path('logout/', include('users.urls')),
    path('users/', include('users.urls')),
    path('', lambda request: redirect('login')),
    path('', lambda request: redirect('user_list')),

]
