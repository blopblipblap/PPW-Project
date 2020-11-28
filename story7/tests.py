from django.test import TestCase, Client
from django.urls import resolve
from .views import story7

# Create your tests here.
class story7(TestCase):
    #Cek URL
    def test_urlnya_ada(self):
        response = Client().get('/story7/')
        self.assertEquals(response.status_code, 200)

    #Cek template
    def test_template_yang_digunakan(self):
        response = Client().get('/story7/')
        self.assertTemplateUsed(response, 'story7/story7.html')