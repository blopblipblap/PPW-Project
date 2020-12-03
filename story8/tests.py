from django.test import TestCase, Client
from django.urls import resolve
from .views import story8, perantara

# Create your tests here.
class story8(TestCase):
    #Cek URL
    def test_urlnya_ada(self):
        response = Client().get('/story8/')
        self.assertEquals(response.status_code, 200)
    
    def test_url_data_ada(self):
        response = Client().get('/story8/data')
        self.assertEquals(response.status_code, 200)

    #Cek template
    def test_template_yang_digunakan(self):
        response = Client().get('/story8/')
        self.assertTemplateUsed(response, 'story8/story8.html')

    #Cek Views
    def test_story8_ada(self):
        found = resolve('/story8/data')
        self.assertEquals(found.func, perantara)
