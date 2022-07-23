from urllib import request
from django.http import HttpRequest
from django.test import TestCase
from todoapp.views import top

class TopPageViewTest(TestCase):
    def test_top_returns_200(self):
        req = HttpRequest()
        res = top(request)
        self.assertEqual(res.status_code, 200)
        
    
    def test_top_returns_expected_content(self):
        req = HttpRequest()
        res = top(request)
        self.assertEqual(res.content, b"Hello World")
