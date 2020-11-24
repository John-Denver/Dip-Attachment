from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
gender = (('Male', 'Male',),  ('Female', 'Female'), ('Others', 'Others'))
blood_type = (('A', 'A'), ('A+', 'A+'), ('A-', 'A-'), ('B', 'B'),
              ('B+', 'B+'), ('B-', 'B-'), ('O', 'O'), ('O+', 'O+'), ('O-', 'O-'),)
consultation_type = (('Online Consultation', 'Online Consultation'),
                     ('Face-Face Consultation', 'Face-Face Consultation'))


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


class Department(models.Model):
    d_name = models.CharField(max_length=30)
    hod = models.CharField(max_length=30)

    def __str__(self):
        return self.d_name


class Doctor(models.Model):
    d_name = models.CharField(max_length=60)
    image = models.ImageField(default='enrc.jpg', upload_to='profile_pics', blank=True)
    bio = models.TextField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    def __str__(self):
        return self.d_name


class Clinician(models.Model):
    c_name = models.CharField(max_length=60)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    def __str__(self):
        return self.c_name


class Medrecs(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="records")
    title = models.CharField(max_length=60, null=True)
    clinician = models.ForeignKey(Clinician, on_delete=models.PROTECT)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now(), null=True)
    meds = models.TextField()

    def __str__(self):
        return self.title

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


class Appointment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="recrds")
    name = models.CharField(max_length=40)
    subject = models.CharField(max_length=60, null=True)
    number = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.subject


class UserAppointment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="recds")
    patient_name = models.CharField(max_length=60, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    date = models.DateTimeField()
    location = models.CharField(max_length=30, null=True)
    reason = models.TextField()

    def __str__(self):
        return self.patient_name


class Consultation(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="cnslt")
    appointment = models.ForeignKey(UserAppointment, on_delete=models.CASCADE)
    consultation_type = models.CharField(max_length=30, choices=consultation_type, default='Online Consultation')
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.PROTECT)
    patient_name = models.CharField(max_length=250)

    def __str__(self):
        return self.consultation_type + '- with' + self.patient_name


class Contact(models.Model):
    clinician = models.ForeignKey(Clinician, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.subject


class Message(models.Model):
    to = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="record")
    clinician = models.ForeignKey(Clinician, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.subject
