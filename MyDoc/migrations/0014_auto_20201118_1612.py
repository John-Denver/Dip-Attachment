# Generated by Django 3.1.3 on 2020-11-18 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyDoc', '0013_auto_20201118_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medrecs',
            name='Patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MyDoc.patient'),
        ),
    ]
