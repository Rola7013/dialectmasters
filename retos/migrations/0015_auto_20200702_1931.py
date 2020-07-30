# Generated by Django 3.0.7 on 2020-07-02 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retos', '0014_auto_20200702_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
