# Generated by Django 3.1.3 on 2020-11-22 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('patient_name', models.CharField(max_length=250)),
                ('doctor', models.CharField(max_length=250)),
                ('time', models.CharField(max_length=250)),
                ('file_number', models.CharField(max_length=20)),
                ('is_doctor', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultation_number', models.CharField(max_length=250)),
                ('doctor_name', models.CharField(max_length=250)),
                ('patient_name', models.CharField(max_length=250)),
                ('file_number', models.CharField(max_length=20)),
                ('is_doctor', models.BooleanField(default=False)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='the_user.appointment')),
            ],
        ),
    ]