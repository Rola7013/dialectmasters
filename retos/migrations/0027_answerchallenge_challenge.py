# Generated by Django 3.0.7 on 2020-07-06 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retos', '0026_answerchallenge'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerchallenge',
            name='challenge',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='retos.Challenge'),
        ),
    ]
