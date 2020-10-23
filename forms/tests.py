from django.test import TestCase, Client
from django.urls import resolve
from .views import forms, savematkul, readmatkul, details, deletematkul
from .models import Matkul

# Create your tests here.
class Form(TestCase):
    #Cek Models
    def setUp(self):
        Matkul.objects.create(
            name="Puff's Boating School",
            dosen="Mrs.Puff",
            sks="3 SKS",
            deskripsi="semoga lulus semester 3 amin",
            semester="1",
            kelas="24 funnier that 25 haha.."
        )

    def test_apakah_ada_model_Matkul(self):
        hitung_berapa_matkul = Matkul.objects.all().count()
        self.assertEquals(hitung_berapa_matkul, 1)

    #Cek URL
    def test_urlnya_ada(self):
        response = Client().get('/forms/')
        self.assertEquals(response.status_code, 200)
    
    def test_url_savematkul_ada(self):
        response = Client().get('/forms/savematkul')
        self.assertEquals(response.status_code, 302) #savematkul hanya redirect

    def test_url_readmatkul_ada(self):
        response = Client().get('/forms/readmatkul')
        self.assertEquals(response.status_code, 200)

    def test_url_details_ada(self):
        response = Client().get('/forms/details/1/')
        self.assertEquals(response.status_code, 200)

    def test_url_delete_ada(self):
        response = Client().get('/forms/details/1/delete/')
        self.assertEquals(response.status_code, 200)

    #Cek Views
    def test_forms_ada(self):
        found = resolve('/forms/')
        self.assertEquals(found.func, forms)

    def test_savematkul_ada(self):
        found = resolve('/forms/savematkul')
        self.assertEquals(found.func, savematkul)

    def test_readmatkul_ada(self):
        found = resolve('/forms/readmatkul')
        self.assertEquals(found.func, readmatkul)

    def test_details_ada(self):
        found = resolve('/forms/details/1/')
        self.assertEquals(found.func, details)

    def test_delete_ada(self):
        found = resolve('forms/details/1/delete/')
        self.assertEquals(found.func, deletematkul)