from django.test import TestCase
from django.urls import reverse


class LinkIndexViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/links/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('info:links_index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('info:links_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'info/links.html')

    def test_links_index_exists(self):
        response = self.client.get(reverse('info:links_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('links_list' in response.context)


class RestaurantIndexViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/restaurants/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('info:restaurant_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('info:restaurant_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'info/restaurant_list.html')

    def test_restaurant_list_exists(self):
        response = self.client.get(reverse('info:restaurant_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('restaurant_list' in response.context)


class AllVeganRestaurantsViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/restaurants/all-vegan/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('info:all_vegan_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('info:all_vegan_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'info/restaurant_list.html')

    def test_restaurant_list_exists(self):
        response = self.client.get(reverse('info:all_vegan_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('restaurant_list' in response.context)


class ShoppingIndexViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/shopping/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('info:shopping_index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('info:shopping_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'info/shopping_index.html')

    def test_farmers_market_list_exists(self):
        response = self.client.get(reverse('info:shopping_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('farmers_market_list' in response.context)

    def test_vegan_com_list_exists(self):
        response = self.client.get(reverse('info:shopping_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('vegan_com_list' in response.context)
