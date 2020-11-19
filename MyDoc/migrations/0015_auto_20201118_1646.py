# Generated by Django 3.1.3 on 2020-11-18 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyDoc', '0014_auto_20201118_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medrecs',
            name='Patient',
        ),
        migrations.RemoveField(
            model_name='medrecs',
            name='user',
        ),
        migrations.AddField(
            model_name='medrecs',
            name='patient',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='MyDoc.patient'),
        ),
    ]