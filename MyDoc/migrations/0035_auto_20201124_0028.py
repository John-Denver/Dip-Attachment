# Generated by Django 3.1.3 on 2020-11-23 21:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MyDoc', '0034_auto_20201124_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='userappointment',
            name='patient_name',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='medrecs',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 23, 21, 28, 31, 782237, tzinfo=utc), null=True),
        ),
    ]
