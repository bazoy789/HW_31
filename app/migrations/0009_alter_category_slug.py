# Generated by Django 4.1.7 on 2023-04-20 19:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(5)]),
        ),
    ]
