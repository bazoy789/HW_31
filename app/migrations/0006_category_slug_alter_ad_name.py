# Generated by Django 4.1.7 on 2023-04-17 18:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_selection'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(default='slug', max_length=10, validators=[django.core.validators.MinLengthValidator(5)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ad',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]