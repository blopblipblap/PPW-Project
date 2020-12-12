from django.test import TestCase, Client
from django.contrib.auth.models import User
from .views import register
from django.urls import resolve, reverse

# Create your tests here.
class story9(TestCase):
    #Cek Model
    def test_apakah_user_dapat_dibuat(self):
        user = User.objects.create_user(
            username='testoke',
            password='oke12345'
        )
        hitung_berapa_user = User.objects.all().count()
        self.assertEquals(hitung_berapa_user, 1)

    #Cek URL
    def test_url_register_ada(self):
        response = Client().get('/register/')
        self.assertEquals(response.status_code, 200)

    def test_url_login_ada(self):
        response = Client().get('/login/')
        self.assertEquals(response.status_code, 200)

    def test_url_logout_ada(self):
        response = Client().get('/logout/')
        self.assertEquals(response.status_code, 200)

    #Cek Views
    def test_views_ada(self):
        found = resolve('/register/')
        self.assertEquals(found.func, register)

    def test_POST_register(self):
        response = self.client.post(reverse('register'), data = 
        {'username': 'testoke',
        'password1':'oke12345',
        'password2': 'oke12345'})
        banyaknya = User.objects.count()
        self.assertEquals(banyaknya, 1)

