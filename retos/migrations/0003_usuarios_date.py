# Generated by Django 3.0.7 on 2020-06-19 16:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('retos', '0002_challenge'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
