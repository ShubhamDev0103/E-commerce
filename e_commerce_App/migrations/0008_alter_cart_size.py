# Generated by Django 3.2.13 on 2022-05-14 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_App', '0007_cart_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Size',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
