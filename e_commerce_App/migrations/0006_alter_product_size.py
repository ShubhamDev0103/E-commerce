# Generated by Django 3.2.13 on 2022-05-13 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_App', '0005_alter_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Size',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
