# pylint: disable=protected-access

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from blog.models import (
    Category,
    Post,
)


class CategoryTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all the test methods
        num_categories = 10
        first_id = 0

        for num_category in range(num_categories):
            if num_category > 0:
                category = Category.objects.create(
                    name=f'Category {num_category}',
                )
            else:
                category = Category.objects.create(
                    name=f'Category {num_category}',
                )
                first_id = category.id

        cls.first_id = first_id
        cls.category1 = Category.objects.get(name='Category 0')
        cls.category2 = Category.objects.get(name='Category 1')

    def test_get_name_level_1(self):
        category = self.category1.get_name()
        self.assertEqual(category, "Category 0")

    def test_get_name_level_2(self):
        category = self.category2.get_name()
        self.assertEqual(category, "Category 1")

    def test_name_label(self):
        category = self.category1
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, "name")

    def test_slug_label(self):
        category = self.category1
        field_label = category._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, "slug")

    def test_object_name_is_category_path_level_1(self):
        category = Category.objects.get(id=self.first_id)
        expected_object_name = 'Category 0'
        self.assertEqual(str(category), expected_object_name)

    def test_object_name_is_category_path_level_2(self):
        category = Category.objects.get(id=self.first_id + 1)
        expected_object_name = 'Category 1'
        self.assertEqual(str(category), expected_object_name)


class PostTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Add an author
        user1 = User.objects.create_user(
            username='test',
            first_name='Test',
            last_name='McTesterson',
        )
        user2 = User.objects.create_user(
            username='test2',
        )
        cls.user1 = user1
        cls.user2 = user2

        # Create a category
        category = Category.objects.create(
            name='Category'
        )
        cls.category = category

        # Add post object
        title = 'A Test Post'
        date_updated = timezone.now()
        content = 'A test post with content.'
        post1 = Post.objects.create(
            title=title,
            author=user1,
            date_updated=date_updated,
            content=content,
            category=category,
        )
        title = 'A Test Post 2'
        date_updated = timezone.now()
        content = 'A second test post with content.'
        post2 = Post.objects.create(
            title=title,
            author=user2,
            date_updated=date_updated,
            content=content,
            category=category,
        )
        cls.post1 = post1
        cls.post2 = post2

    def test_title_label(self):
        post = self.post1
        field_label = post._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_author_label(self):
        post = self.post1
        field_label = post._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_date_created_label(self):
        post = self.post1
        field_label = post._meta.get_field('date_created').verbose_name
        self.assertEqual(field_label, 'date created')

    def test_date_updated_label(self):
        post = self.post1
        field_label = post._meta.get_field('date_updated').verbose_name
        self.assertEqual(field_label, 'date updated')

    def test_category_label(self):
        post = self.post1
        field_label = post._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    def test_content_label(self):
        post = self.post1
        field_label = post._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')

    def test_status_label(self):
        post = self.post1
        field_label = post._meta.get_field('status').verbose_name
        self.assertEqual(field_label, 'status')

    def test_slug_label(self):
        post = self.post1
        field_label = post._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')

    def test_object_name_is_title(self):
        post = self.post1
        expected_object_name = post.title
        self.assertEqual(str(post), expected_object_name)

    def test_object_author_has_no_name(self):
        post = self.post2
        author = self.user2
        expected_object_name = author.username
        self.assertEqual(str(post.get_author()), expected_object_name)

    def test_object_author_is_author_full_name(self):
        post = self.post1
        author = self.user1
        expected_object_name = author.get_full_name()
        self.assertEqual(str(post.get_author()), expected_object_name)
