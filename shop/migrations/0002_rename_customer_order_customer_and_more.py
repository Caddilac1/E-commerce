# Generated by Django 5.1.2 on 2024-10-14 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Customer',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='Product',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='Customer',
            new_name='customer',
        ),
    ]
