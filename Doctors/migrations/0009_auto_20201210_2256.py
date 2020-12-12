# Generated by Django 3.1.3 on 2020-12-10 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Doctors', '0008_auto_20201210_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, default='nurse.jpg', upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='dcts', to=settings.AUTH_USER_MODEL),
        ),
    ]