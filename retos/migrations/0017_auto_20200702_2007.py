# Generated by Django 3.0.7 on 2020-07-02 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retos', '0016_auto_20200702_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email address'),
        ),
    ]
