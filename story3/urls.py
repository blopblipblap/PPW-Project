from django.urls import include, path
from .views import aboutme, myexperience

urlpatterns = [
    path('aboutme/', aboutme, name='aboutme'),
    path('myexperience/', myexperience, name='myexperience'),
]