# Generated by Django 3.2.3 on 2021-06-01 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_vegancompany'),
    ]

    operations = [
        migrations.AddField(
            model_name='vegancompany',
            name='website',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
