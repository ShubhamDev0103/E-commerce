# Generated by Django 3.2.13 on 2022-05-12 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_commerce_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Size',
            field=models.PositiveSmallIntegerField(default='1'),
        ),
    ]