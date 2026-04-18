from django.test import TestCase
from django.urls import reverse

class PageAccessTest(TestCase):
    def test_pages_load(self):
        pages = ['index', 'services', 'projects', 'about', 'contact']
        for page in pages:
            response = self.client.get(reverse(page))
            self.assertEqual(response.status_code, 200, f"Page {page} failed to load.")
