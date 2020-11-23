# Generated by Django 3.1.3 on 2020-11-23 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('the_user', '0003_auto_20201123_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
