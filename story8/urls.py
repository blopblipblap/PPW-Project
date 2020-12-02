from django.urls import include, path
from .views import story8

urlpatterns = [
    path('', story8, name='story8'),
]