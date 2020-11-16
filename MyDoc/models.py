from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
gender = (('Male', 'Male',),  ('Female', 'Female'), ('Others', 'Others'))
blood_type = (('A', 'A'), ('A+', 'A+'), ('A-', 'A-'), ('B', 'B'),
              ('B+', 'B+'), ('B-', 'B-'), ('O', 'O'), ('O+', 'O+'), ('O-', 'O-'),)


class Patient(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=60)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices=gender, default='Male')
    email = models.EmailField(blank=True)
    contact = models.IntegerField()
    blood_type = models.CharField(max_length=5, choices=blood_type, default='O')

    def __str__(self):
        return self.username


class PatientRec(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=20)
    song_file = models.FileField()

    def __str__(self):
        return self.song_name

""""
class Profile(models.Model):
    choices = (("Yes", 'Yes'), ("No", 'No'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    Email = models.EmailField(default='none@email.com')
    Malaria = models.CharField(max_length=255, choices=choices)
    Diarrheal_Diseases = models.CharField(max_length=255, choices=choices)
    Road_Injuries = models.CharField(max_length=255, choices=choices)
    Tuberculosis = models.CharField(max_length=255, choices=choices)
    Cough = models.CharField(max_length=255, choices=choices)

    def __str__(self):
        return f'{self.user.username} Profile'"""


class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.subject


class Appointment(models.Model):
    name = models.CharField(max_length=40)
    id_number = models.IntegerField()
    number = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()
    image = models.FileField()

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.subject

