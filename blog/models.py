from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

POST_STATUS = (
	(0, "Draft"),
	(1, "Publish"),
)


class Post(models.Model):
	title = models.CharField(max_length=200, unique=True)
	author = models.ForeignKey(
		User,
		on_delete=models.CASCADE

	)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	content = models.TextField()
	status = models.IntegerField(choices=POST_STATUS, default=0)
	slug = models.SlugField(
		max_length=200,
		unique=True,
		editable=False,
	)

	class Meta:
		ordering = ['-date_created']

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		value = self.title
		self.slug = slugify(value, allow_unicode=True)
		super().save(*args, **kwargs)
