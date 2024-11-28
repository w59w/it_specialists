
from django.shortcuts import redirect
from django.conf import settings
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('users.urls')),
    path('login/', include('users.urls')),
    path('logout/', include('users.urls')),
    path('users/', include('users.urls')),
    path('', lambda request: redirect('login')),
    path('', lambda request: redirect('user_list')),

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
