from django.urls import include, path
from .views import forms, savematkul, readmatkul, details, deletematkul

urlpatterns = [
    path('', forms, name='forms'),
    path('savematkul', savematkul),
    path('readmatkul', readmatkul, name='read'),
    path('details/<int:angka>/', details, name='details'),
    path('details/<int:angka>/delete/', deletematkul)
]