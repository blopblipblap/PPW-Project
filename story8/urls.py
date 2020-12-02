from django.urls import include, path
from .views import story8, perantara

urlpatterns = [
    path('', story8, name='story8'),
    path('data', perantara, name='story8'),
]