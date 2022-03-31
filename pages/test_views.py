from django.contrib.auth.models import User
from django.test import TestCase

from .models import Page

class IndexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all the test methods
        author = User.objects.create(
            username='test',
            first_name='Test',
            last_name='McTesterson'
        )

        page = Page.objects.create(
            title='Index',
            path='index',
            author=author,
        )

        cls.page = page

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_path(self):
        response = self.client.get(f'/{self.page.path}/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/index.html')
