from django.db import models

# Create your models here.

class Kegiatan(models.Model):
    nama = models.CharField(max_length=150)

    def __str__(self):
        return self.nama

class Orang(models.Model):
    orang = models.CharField(max_length=150)
    kegiatan = models.ForeignKey(Kegiatan, on_delete=models.CASCADE)

    def __str__(self):
        return self.orang
