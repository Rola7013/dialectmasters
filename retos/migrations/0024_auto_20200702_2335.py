# Generated by Django 3.0.7 on 2020-07-02 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retos', '0023_auto_20200702_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='user_language_learning',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='retos.Language_learning'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='user_language_native',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='retos.Language_native'),
        ),
    ]
