# Generated by Django 4.0.2 on 2022-02-27 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_vegancompany_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmersmarket',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]