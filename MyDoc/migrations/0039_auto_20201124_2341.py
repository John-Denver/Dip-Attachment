# Generated by Django 3.1.3 on 2020-11-24 20:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MyDoc', '0038_auto_20201124_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='last_check',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 11, 24, 20, 41, 33, 661874, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='patient',
            name='next_check',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 11, 24, 20, 41, 33, 661874, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='medrecs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 24, 20, 41, 33, 677502, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='userappointment',
            name='consultation_type',
            field=models.CharField(blank=True, choices=[('', ''), ('Online Consultation', 'Online Consultation'), ('Face-Face Consultation', 'Face-Face Consultation')], default='No consultation', max_length=30),
        ),
    ]