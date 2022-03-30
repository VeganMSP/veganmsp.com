# pylint: disable=missing-module-docstring,
# pylint: disable=missing-class-docstring,
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name

from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from blog.models import (
    Category,
    Post,
)


class IndexViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')


class CategoryDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create category object
        category = Category.objects.create(
            name='Category'
        )
        cls.category = category

    def test_view_url_exists_at_desired_location(self):
        category = self.category
        response = self.client.get(f'/blog/category/{category.slug}/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        category = self.category
        response = self.client.get(
            reverse('blog:category_detail', args=[category.slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/category_detail.html')


class PostCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create the user
        user = User.objects.create_user(
            username='test',
            password='secret',
        )
        cls.user = user

        # Create category object
        category = Category.objects.create(
            name='Category'
        )
        cls.category = category

        authenticated_client = Client()
        authenticated_client.login(username='test', password='secret')
        cls.authenticated_client = authenticated_client

    def test_view_url_unauthenticated(self):
        url = '/blog/add/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_view_url_exists_at_desired_location(self):
        response = self.authenticated_client.get('/blog/add/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.authenticated_client.get(reverse('blog:post_create'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.authenticated_client.get(reverse('blog:post_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')

    def test_valid_post(self):
        response = self.authenticated_client.post(
            reverse('blog:post_create'),
            {
                'title': 'My blog title',
                'author': self.user,
                'category': self.category.id,
                'content': 'Post content!',
                'status': 0
            }
        )
        self.assertTrue(response.status_code, 200)


class PostUpdateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create the user
        user = User.objects.create_user(
            username='test',
            password='secret',
        )
        cls.user = user

        # Create a category
        category = Category.objects.create(
            name='Category'
        )
        cls.category = category

        # Create a post
        post = Post.objects.create(
            title='My blog title',
            author=user,
            category=category,
            status=0,
            content='My post content',
        )
        cls.post = post

        authenticated_client = Client()
        authenticated_client.login(username='test', password='secret')
        cls.authenticated_client = authenticated_client

    def test_view_url_unauthenticated(self):
        slug = self.post.slug
        url = f'/blog/add/{slug}/'
        response = self.client.get(url)
        self.assertTrue(response.status_code, 404)

    def test_view_url_exists_at_desired_location(self):
        slug = self.post.slug
        response = self.authenticated_client.get(f'/blog/edit/{slug}/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        slug = self.post.slug
        response = self.authenticated_client.get(
            reverse('blog:post_update', args=[slug])
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        slug = self.post.slug
        response = self.authenticated_client.get(
            reverse('blog:post_update', args=[slug])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')


class PostDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create the user
        user = User.objects.create_user(
            username='test',
            password='secret',
        )
        cls.user = user

        # Create a category
        category = Category.objects.create(
            name='Category'
        )
        cls.category = category

        # Create a post
        post = Post.objects.create(
            title='My blog title',
            author=user,
            category=category,
            status=0,
            content='My post content'
        )
        cls.post = post

        authenticated_client = Client()
        authenticated_client.login(username='test', password='secret')
        cls.authenticated_client = authenticated_client

    def test_view_url_unauthenticated(self):
        slug = self.post.slug
        url = f'/blog/_d/{slug}/'
        response = self.client.get(url)
        self.assertTrue(response.status_code, 404)

    def test_view_url_exists_at_desired_location(self):
        slug = self.post.slug
        response = self.authenticated_client.get(f'/blog/_d/{slug}/')
        self.assertTrue(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        slug = self.post.slug
        response = self.authenticated_client.get(
            reverse('blog:post_delete', args=[slug])
        )
        self.assertTrue(response.status_code, 200)

    def test_view_404_delete_nonexistent_item(self):
        slug = self.post.slug + "nonsense"
        response = self.authenticated_client.get(
            reverse('blog:post_delete', args=[slug])
        )
        self.assertEqual(response.status_code, 404)

    def test_valid_post(self):
        post = self.post
        slug = post.slug

        response = self.authenticated_client.post(
            reverse('blog:post_delete', args=[slug])
        )
        self.assertRedirects(
            response,
            expected_url=reverse('blog:index'),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True
        )
