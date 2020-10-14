from django.urls import include, path
from .views import forms, savematkul, readmatkul

urlpatterns = [
    path('', forms, name='forms'),
    path('savematkul', savematkul),
    path('readmatkul', readmatkul),
]