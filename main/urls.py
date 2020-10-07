from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('myexperience/', views.myexperience, name='myexperience'),
    path('story1/', views.story1, name='story1'),
]
