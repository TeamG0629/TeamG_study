# Generated by Django 3.2.7 on 2022-10-28 04:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('precomi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='precycle',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(8), django.core.validators.MaxValueValidator(8)]),
        ),
    ]