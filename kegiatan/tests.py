from django.test import TestCase, Client
from django.urls import resolve
from .views import savekegiatan, kegiatann, details, saveorang
from .models import Kegiatan, Orang
from django.contrib.admin.sites import AdminSite
from .admin import Kegiatan, Orang

# Create your tests here.
class kegiatan(TestCase):
    #Cek Model
    def setUp(self):
        self.kegiatan = Kegiatan.objects.create(nama="HALO")
        self.orang = Orang.objects.create(orang="VANE", kegiatan=self.kegiatan)

    def test_apakah_ada_model_kegiatan(self):
        hitung_berapa_banyak = Kegiatan.objects.all().count()
        self.assertEquals(hitung_berapa_banyak, 1)

    def test_apakah_ada_model_orang(self):
        hitung_berapa_banyak_orang = Orang.objects.all().count()
        self.assertEquals(hitung_berapa_banyak_orang, 1)
    
    def test_string_kegiatan(self):
        self.assertEqual(str(self.kegiatan), self.kegiatan.nama)

    def test_string_orang(self):
        self.assertEqual(str(self.orang), self.orang.orang)

    #Cek URL
    def test_urlnya_ada(self):
        response = Client().get('/kegiatan/')
        self.assertEquals(response.status_code, 200)

    def test_url_savekegiatan_ada(self):
        response = Client().get('/kegiatan/savekegiatan')
        self.assertEquals(response.status_code, 302) #Karena savekegiatan hanya redirect

    def test_url_details_ada(self):
        response = Client().get('/kegiatan/details/1/')
        self.assertEquals(response.status_code, 200)

    def test_url_saveorang_ada(self):
        response = Client().get('/kegiatan/details/1/saveorang')
        self.assertEquals(response.status_code, 302) #Karena hanya redirect

    #Cek Template
    def test_template_yang_digunakan(self):
        response = Client().get('/kegiatan/')
        self.assertTemplateUsed(response, 'kegiatan/kegiatan.html')

    def test_apakah_ada_text_daftar_kegiatan(self):
        response = Client().get('/kegiatan/')
        html_kembalian = response.content.decode('utf8')
        self.assertIn("Daftar Kegiatan", html_kembalian)

    #Cek Views
    def test_kegiatan_ada(self):
        found = resolve('/kegiatan/')
        self.assertEquals(found.func, kegiatann)

    def test_savekegiatan_ada(self):
        found = resolve('/kegiatan/savekegiatan')
        self.assertEquals(found.func, savekegiatan)

    def test_details_ada(self):
        found = resolve('/kegiatan/details/1/')
        self.assertEquals(found.func, details)

    def test_saveorang_ada(self):
        found = resolve('/kegiatan/details/1/saveorang')
        self.assertEquals(found.func, saveorang)
        