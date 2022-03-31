# pylint: disable=protected-access

from django.contrib.auth.models import User
from django.test import TestCase

from .models import (
    Page
)


class PageModelTestCase(TestCase):
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

    def test_title_label(self):
        page = self.page
        field_label = page._meta.get_field('title').verbose_name
        self.assertEqual(field_label, "title")

    def test_slug_label(self):
        page = self.page
        field_label = page._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, "slug")

    def test_date_created_label(self):
        page = self.page
        field_label = page._meta.get_field('date_created').verbose_name
        self.assertEqual(field_label, "date created")

    def test_date_updated_label(self):
        page = self.page
        field_label = page._meta.get_field('date_updated').verbose_name
        self.assertEqual(field_label, "date updated")

    def test_verbose_name_plural(self):
        page = self.page
        verbose_name_plural = page._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, "pages")

    def test_object_name_is_title(self):
        page = self.page
        expected_object_name = page.title
        self.assertEqual(str(page), expected_object_name)
