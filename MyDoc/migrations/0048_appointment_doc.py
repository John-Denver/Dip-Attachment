# Generated by Django 3.1.3 on 2020-12-10 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0015_remove_doctor_bio'),
        ('MyDoc', '0047_auto_20201204_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doc',
            field=models.ForeignKey(default='Myself', on_delete=django.db.models.deletion.PROTECT, related_name='dcts', to='Doctors.doctor'),
        ),
    ]