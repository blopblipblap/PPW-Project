from django.urls import include, path
from .views import kegiatann, savekegiatan, details, saveorang

urlpatterns = [
    path('', kegiatann, name='kegiatan'),
    path('savekegiatan', savekegiatan),
    path('details/<int:angka>/', details, name='detailkeg'),
    path('details/<int:angka>/saveorang', saveorang)
]