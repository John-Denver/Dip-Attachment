# Generated by Django 3.1.3 on 2020-11-16 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MyDoc', '0004_auto_20201116_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
