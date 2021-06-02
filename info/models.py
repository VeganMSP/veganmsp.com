from django.db import models
from django.utils.text import slugify


class City(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Neighborhood(models.Model):
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	description = models.TextField(blank=True)
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Address(models.Model):
	name = models.CharField(max_length=200, blank=True)
	street1 = models.CharField(max_length=200, blank=True)
	street2 = models.CharField(max_length=200, blank=True)
	city = models.ForeignKey(City, on_delete=models.CASCADE)
	state = models.CharField(max_length=2)
	zip_code = models.CharField(max_length=10, blank=True)

	def __str__(self):
		if self.name != "":
			return self.name
		elif self.street1 != "":
			return self.street1 + " - " + self.city.name
		else:
			return self.city.name


class RestaurantLocation(models.Model):
	address = models.ForeignKey(Address, on_delete=models.CASCADE)
	phone = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return self.address.city.name


class Restaurant(models.Model):
	name = models.CharField(max_length=200)
	location = models.ForeignKey(RestaurantLocation, on_delete=models.CASCADE)
	date_created = models.DateTimeField('date_published', auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	slug = models.SlugField(
		max_length=200,
		editable=False,
		unique=True
	)
	website = models.CharField(blank=True, max_length=2000)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		value = self.name
		self.slug = slugify(value, allow_unicode=True)
		super().save(*args, **kwargs)


class FarmersMarket(models.Model):
	address = models.ForeignKey(Address, on_delete=models.CASCADE)
	hours = models.TextField(blank=True)
	name = models.CharField(max_length=200)
	phone = models.CharField(max_length=20, blank=True)
	website = models.CharField(max_length=2000, blank=True)

	def __str__(self):
		return self.name


class VeganCompany(models.Model):
	name = models.CharField(max_length=200)
	website = models.CharField(max_length=2000, blank=True)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name


class LinkCategory(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name


class Link(models.Model):
	name = models.CharField(max_length=200)
	website = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	category = models.ForeignKey(LinkCategory, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
