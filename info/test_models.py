# pylint: disable=missing-module-docstring,
# pylint: disable=missing-class-docstring,
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=protected-access

from django.test import TestCase

from info.models import (
    City,
    Address,
    Restaurant,
    FarmersMarket,
    VeganCompany,
    LinkCategory,
    Link,
)


class CityModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all the test methods
        city = City.objects.create(
            name='Simpletown',
        )

        cls.city = city

    def test_name_label(self):
        city = self.city
        field_label = city._meta.get_field('name').verbose_name
        self.assertEqual(field_label, "name")

    def test_slug_label(self):
        city = self.city
        field_label = city._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, "slug")

    def test_date_created_label(self):
        city = self.city
        field_label = city._meta.get_field('date_created').verbose_name
        self.assertEqual(field_label, "date created")

    def test_date_updated_label(self):
        city = self.city
        field_label = city._meta.get_field('date_updated').verbose_name
        self.assertEqual(field_label, "date updated")

    def test_verbose_name_plural(self):
        city = self.city
        verbose_name_plural = city._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, "cities")

    def test_object_name_is_name(self):
        city = self.city
        expected_object_name = city.name
        self.assertEqual(str(city), expected_object_name)


class AddressModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all the test methods
        city = City.objects.create(
            name='Simpletown',
        )
        cls.city = city

        address = Address.objects.create(
            city=city,
            name='1234 Simple Street',
            street1='1234 Simple Street',
            state='PA',
        )
        cls.address = address

    def test_name_label(self):
        address = self.address
        field_label = address._meta.get_field('name').verbose_name
        self.assertEqual(field_label, "name")

    def test_street1_label(self):
        address = self.address
        field_label = address._meta.get_field('street1').verbose_name
        self.assertEqual(field_label, "street1")

    def test_street2_label(self):
        address = self.address
        field_label = address._meta.get_field('street2').verbose_name
        self.assertEqual(field_label, "street2")

    def test_city_label(self):
        address = self.address
        field_label = address._meta.get_field('city').verbose_name
        self.assertEqual(field_label, "city")

    def test_state_label(self):
        address = self.address
        field_label = address._meta.get_field('state').verbose_name
        self.assertEqual(field_label, "state")

    def test_zip_code_label(self):
        address = self.address
        field_label = address._meta.get_field('zip_code').verbose_name
        self.assertEqual(field_label, "zip code")

    def test_verbose_name_plural(self):
        address = self.address
        verbose_name_plural = address._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, "addresses")

    def test_object_name_is_name_when_name_exists(self):
        address = self.address
        expected_object_name = address.name
        self.assertEqual(str(address), expected_object_name)

    def test_object_name_is_name_when_name_not_exists(self):
        address = Address.objects.create(
            street1='1234 Simple Street',
            city=self.city,
        )
        expected_object_name = address.street1 + ' - ' + address.city.name
        self.assertEqual(str(address), expected_object_name)

    def test_object_name_is_name_when_name_or_street1_not_exists(self):
        address = Address.objects.create(
            city=self.city,
        )
        expected_object_name = address.city.name
        self.assertEqual(str(address), expected_object_name)


class RestaurantModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all the test methods
        city = City.objects.create(
            name='Simpletown',
        )
        cls.city = city

        restaurant = Restaurant.objects.create(
            name='Phil\'s Pizza',
            location=city
        )
        cls.restaurant = restaurant

    def test_name_label(self):
        restaurant = self.restaurant
        field_label = restaurant._meta.get_field('name').verbose_name
        self.assertEqual(field_label, "name")

    def test_location_label(self):
        restaurant = self.restaurant
        field_label = restaurant._meta.get_field('location').verbose_name
        self.assertEqual(field_label, "location")

    def test_date_created_label(self):
        restaurant = self.restaurant
        field_label = restaurant._meta.get_field('date_created').verbose_name
        self.assertEqual(field_label, "date_published")

    def test_date_updates_label(self):
        restaurant = self.restaurant
        field_label = restaurant._meta.get_field('date_updated').verbose_name
        self.assertEqual(field_label, "date updated")

    def test_slug_label(self):
        restaurant = self.restaurant
        field_label = restaurant._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, "slug")

    def test_website_label(self):
        restaurant = self.restaurant
        field_label = restaurant._meta.get_field('website').verbose_name
        self.assertEqual(field_label, "website")

    def test_description_label(self):
        restaurant = self.restaurant
        field_label = restaurant._meta.get_field('description').verbose_name
        self.assertEqual(field_label, "description")

    def test_all_vegan_label(self):
        restaurant = self.restaurant
        field_label = restaurant._meta.get_field('all_vegan').verbose_name
        self.assertEqual(field_label, "all vegan")

    def test_verbose_name_plural(self):
        restaurant = self.restaurant
        verbose_name_plural = restaurant._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, "restaurants")

    def test_object_name_is_restaurant_name(self):
        restaurant = self.restaurant
        expected_object_name = restaurant.name
        self.assertEqual(str(restaurant), expected_object_name)


class FarmersMarketModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all the test methods
        city = City.objects.create(
            name='Simpletown',
        )
        cls.city = city

        address = Address.objects.create(
            city=city,
            name='1234 Simple Street',
            street1='1234 Simple Street',
            state='PA',
        )
        cls.address = address

        farmers_market = FarmersMarket.objects.create(
            address=address,
            name='Simpletown Farmer\'s Market',
        )
        cls.farmers_market = farmers_market

    def test_name_label(self):
        farmers_market = self.farmers_market
        field_label = farmers_market._meta.get_field('name').verbose_name
        self.assertEqual(field_label, "name")

    def test_address_label(self):
        farmers_market = self.farmers_market
        field_label = farmers_market._meta.get_field('address').verbose_name
        self.assertEqual(field_label, "address")

    def test_hours_label(self):
        farmers_market = self.farmers_market
        field_label = farmers_market._meta.get_field('hours').verbose_name
        self.assertEqual(field_label, "hours")

    def test_phone_label(self):
        farmers_market = self.farmers_market
        field_label = farmers_market._meta.get_field('phone').verbose_name
        self.assertEqual(field_label, "phone")

    def test_website_label(self):
        farmers_market = self.farmers_market
        field_label = farmers_market._meta.get_field('website').verbose_name
        self.assertEqual(field_label, "website")

    def test_object_name_is_name(self):
        farmers_market = self.farmers_market
        expected_object_name = farmers_market.name
        self.assertEqual(str(farmers_market), expected_object_name)

    def test_verbose_name_plural(self):
        farmers_market = self.farmers_market
        verbose_name_plural = farmers_market._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, "farmers markets")


class VeganCompanyModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        vegan_company = VeganCompany.objects.create(
            name='My Vegan Shoe Co.',
        )
        cls.vegan_company = vegan_company

    def test_name_label(self):
        vegan_company = self.vegan_company
        field_label = vegan_company._meta.get_field('name').verbose_name
        self.assertEqual(field_label, "name")

    def test_website_label(self):
        vegan_company = self.vegan_company
        field_label = vegan_company._meta.get_field('website').verbose_name
        self.assertEqual(field_label, "website")

    def test_description_label(self):
        vegan_company = self.vegan_company
        field_label = vegan_company._meta.get_field('description').verbose_name
        self.assertEqual(field_label, "description")

    def test_object_name_is_name(self):
        vegan_company = self.vegan_company
        expected_object_name = vegan_company.name
        self.assertEqual(str(vegan_company), expected_object_name)

    def test_verbose_name_plural(self):
        vegan_company = self.vegan_company
        verbose_name_plural = vegan_company._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, "vegan companies")


class LinkCategoryModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all the test methods
        num_link_categories = 10
        last_id = 0
        first_id = 0

        for num_category in range(num_link_categories):
            if num_category > 0:
                link_category = LinkCategory.objects.create(
                    name=f'Link Category {num_category}',
                    parent=LinkCategory.objects.get(id=last_id),
                )
            else:
                link_category = LinkCategory.objects.create(
                    name=f'Link Category {num_category}',
                )
                first_id = link_category.id
            last_id = link_category.id

        cls.first_id = first_id
        cls.link_category1 = LinkCategory.objects.get(name='Link Category 0')
        cls.link_category2 = LinkCategory.objects.get(name='Link Category 1')

    def test_get_name_level_1(self):
        link_category = self.link_category1.get_name()
        self.assertEqual(link_category, "Link Category 0")

    def test_get_name_level_2(self):
        link_category = self.link_category2.get_name()
        self.assertEqual(link_category, "Link Category 1")

    def test_name_label(self):
        link_category = self.link_category1
        field_label = link_category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, "name")

    def test_slug_label(self):
        link_category = self.link_category1
        field_label = link_category._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, "slug")

    def test_parent_label(self):
        link_category = self.link_category1
        field_label = link_category._meta.get_field('parent').verbose_name
        self.assertEqual(field_label, "parent")

    def test_object_name_is_link_category_path_level_1(self):
        link_category = LinkCategory.objects.get(id=self.first_id)
        expected_object_name = 'Link Category 0'
        self.assertEqual(str(link_category), expected_object_name)

    def test_object_name_is_link_category_path_level_2(self):
        link_category = LinkCategory.objects.get(id=self.first_id + 1)
        expected_object_name = 'Link Category 0 -> Link Category 1'
        self.assertEqual(str(link_category), expected_object_name)

    def test_object_name_is_link_category_path_level_3(self):
        link_category = LinkCategory.objects.get(id=self.first_id + 2)
        expected_object_name = 'Link Category 0 -> Link Category 1 -> Link Category 2'
        self.assertEqual(str(link_category), expected_object_name)

    def test_object_name_is_link_category_path_level_4(self):
        link_category = LinkCategory.objects.get(id=self.first_id + 3)
        expected_object_name = 'Link Category 0 -> Link Category 1 -> Link Category 2 -> Link Category 3'  # pylint: disable=line-too-long
        self.assertEqual(str(link_category), expected_object_name)


class LinkModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):

        # Create a link category
        link_category = LinkCategory.objects.create(
            name='Link Category'
        )
        cls.link_category = link_category

        # Add link object
        link = Link.objects.create(
            name='A link',
            website='https://example.com',
            category=link_category,
        )
        cls.link = link

    def test_name_label(self):
        link = self.link
        field_label = link._meta.get_field('name').verbose_name
        self.assertEqual(field_label, "name")

    def test_website_label(self):
        link = self.link
        field_label = link._meta.get_field('website').verbose_name
        self.assertEqual(field_label, "website")

    def test_description_label(self):
        link = self.link
        field_label = link._meta.get_field('description').verbose_name
        self.assertEqual(field_label, "description")

    def test_category_label(self):
        link = self.link
        field_label = link._meta.get_field('category').verbose_name
        self.assertEqual(field_label, "category")

    def test_object_name_is_name(self):
        link = self.link
        expected_object_name = link.name
        self.assertEqual(str(link), expected_object_name)
