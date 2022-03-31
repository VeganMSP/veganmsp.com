from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Page(models.Model):
    title = models.CharField(max_length=200)
    path = models.CharField(
        max_length=200,
        help_text='Without proceeding or appending slashes'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        editable=False
    )
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        slug = self.title
        self.slug = slugify(slug, allow_unicode=True)

        self.date_updated = timezone.now()

        super().save(*args, **kwargs)

    def get_name(self):
        return self.title

    def __str__(self):
        return self.get_name()
