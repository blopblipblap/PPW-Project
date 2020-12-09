"""story4vanessa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from story9.views import register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('story1/', include('story1.urls')),
    path('story3/', include('story3.urls')),
    path('forms/', include('forms.urls')),
    path('kegiatan/', include('kegiatan.urls')),
    path('story7/', include('story7.urls')),
    path('story8/', include('story8.urls')),
    #Story 9
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='story9/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='story9/logout.html'), name='logout'),


]
