# Generated by Django 3.2.13 on 2022-05-16 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_App', '0011_remove_cart_cart_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_c',
            field=models.IntegerField(default=0),
        ),
    ]