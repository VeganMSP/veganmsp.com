# Generated by Django 4.0.2 on 2022-03-31 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='path',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]