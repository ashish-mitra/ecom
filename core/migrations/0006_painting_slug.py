# Generated by Django 5.1 on 2024-09-04 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_painting_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
