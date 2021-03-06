# Generated by Django 3.0.7 on 2020-07-02 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retos', '0020_auto_20200702_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='safe_question',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='user_language_learning',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retos.Language_learning'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='user_language_native',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retos.Language_native'),
        ),
    ]
