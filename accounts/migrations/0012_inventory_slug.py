# Generated by Django 3.1 on 2020-10-04 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20201004_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]