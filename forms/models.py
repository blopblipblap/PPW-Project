from django.db import models

# Create your models here.
class Matkul(models.Model):
    name = models.CharField(max_length=150)
    dosen = models.CharField(max_length=150)
    sks = models.CharField(max_length=150)
    deskripsi = models.TextField(max_length=150)
    semester = models.CharField(max_length=150)
    kelas = models.CharField(max_length=150)