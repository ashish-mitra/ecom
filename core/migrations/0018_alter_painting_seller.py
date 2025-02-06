# Generated by Django 5.1 on 2025-01-02 11:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_painting_seller'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='seller',
            field=models.ForeignKey(default='hero', limit_choices_to={'profile__is_seller': True}, on_delete=django.db.models.deletion.CASCADE, related_name='paintings', to=settings.AUTH_USER_MODEL),
        ),
    ]
