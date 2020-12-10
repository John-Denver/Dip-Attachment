import django
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=60)
    speciality = models.CharField(max_length=50)

    def __str__(self):
        return self.doctor_name


class Patient(models.Model):
    patient_name = models.CharField(max_length=60)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    registration_date = models.DateTimeField("Date registered", auto_now=True)
    waiting_status = models.BooleanField(default=True)

    def __str__(self):
        return self.patient_name

    @property
    def is_waiting(self):
        return bool(self.waiting_status)

