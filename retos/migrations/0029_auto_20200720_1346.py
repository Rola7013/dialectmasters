# Generated by Django 3.0.7 on 2020-07-20 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retos', '0028_auto_20200720_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='second_user_language_learnin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_language', to='retos.Language_learning'),
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='user_language_learning',
        ),
        migrations.AddField(
            model_name='usuarios',
            name='user_language_learning',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='retos.Language_learning'),
        ),
    ]
