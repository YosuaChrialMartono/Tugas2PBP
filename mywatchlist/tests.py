from urllib import response
from django.test import TestCase, Client
from django.urls import resolve
from .views import show_mywatchlist

# Create your tests here.
class WatchlistTest(TestCase):
    def test_show_html(self):
        response = Client().get('/mywatchlist/html', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_show_xml(self):
        response = Client().get('/mywatchlist/xml', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_show_json(self):
        response = Client().get('/mywatchlist/json', follow=True)
        self.assertEqual(response.status_code, 200)