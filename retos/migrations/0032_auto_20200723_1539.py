# Generated by Django 3.0.7 on 2020-07-23 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retos', '0031_auto_20200723_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postuser',
            name='user_language_native',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='retos.Language_native'),
        ),
    ]
