from django.urls import include, path
from .views import story7

urlpatterns = [
    path('', story7, name='story7'),
]