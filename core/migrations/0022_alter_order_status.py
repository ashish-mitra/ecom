# Generated by Django 5.1 on 2025-03-05 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_alter_order_date_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Placed', 'Placed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Placed', max_length=20),
        ),
    ]
