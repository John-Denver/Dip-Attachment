# Generated by Django 3.1.3 on 2020-12-09 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='name',
            new_name='patient_name',
        ),
    ]
