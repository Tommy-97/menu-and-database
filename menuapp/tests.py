#test.py
from django.test import TestCase
from django.urls import reverse

from .models import MenuItem


class MenuItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        MenuItem.objects.create(title='Test Item', url='/test/', order=1)

    def test_title_content(self):
        menu_item = MenuItem.objects.get(id=1)
        expected_title = f'{menu_item.title}'
        self.assertEqual(expected_title, 'Test Item')

    def test_get_absolute_url(self):
        menu_item = MenuItem.objects.get(id=1)
        self.assertEqual(menu_item.get_absolute_url(), '/test/')

class MyPageViewTest(TestCase):
    def test_my_page_view_status_code(self):
        response = self.client.get('/my-page/')
        self.assertEqual(response.status_code, 200)

    def test_my_page_view_template(self):
        response = self.client.get('/my-page/')
        self.assertTemplateUsed(response, 'my_page.html')

    
