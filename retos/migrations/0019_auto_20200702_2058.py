# Generated by Django 3.0.7 on 2020-07-02 20:58

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('retos', '0018_auto_20200702_2046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('safe_question', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('user_language_learning', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retos.Language_learning')),
                ('user_language_native', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retos.Language_native')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='postuser',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
