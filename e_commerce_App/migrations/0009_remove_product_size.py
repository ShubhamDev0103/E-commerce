# Generated by Django 3.2.13 on 2022-05-14 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_App', '0008_alter_cart_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Size',
        ),
    ]
