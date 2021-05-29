from django.db import models

class Restaurant(models.Model):
	name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date_published')
	website = models.CharField(max_length=2000)

	def __str__(self):
		return self.name
