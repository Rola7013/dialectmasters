# Generated by Django 3.0.7 on 2020-06-25 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retos', '0005_auto_20200625_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postuser',
            name='challenge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_user', to='retos.Challenge'),
        ),
    ]
