from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from mptt.models import MPTTModel, TreeForeignKey

POST_STATUS = (
    (0, "Draft"),
    (1, "Publish"),
)


class Category(MPTTModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(
        unique=True,
        editable=False,
    )
    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='child',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])

    def get_name(self):
        return self.name

    def save(self, *args, **kwargs):
        slug = self.name
        self.slug = slugify(slug, allow_unicode=True)
        super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE

    )
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField()
    content = models.TextField()
    category = models.ForeignKey(
        Category,
        related_name='posts',
        on_delete=models.CASCADE
    )
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

    def get_author(self):
        author = self.author.get_full_name()
        if author == '':
            author = self.author
        return author

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)

        self.date_updated = timezone.now()

        super().save(*args, **kwargs)
