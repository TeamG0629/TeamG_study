# Generated by Django 3.2.7 on 2023-02-07 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('precomi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]