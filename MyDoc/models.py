import django
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser

from django.contrib.auth.decorators import login_required

# Create your models here.
gender = (('Male', 'Male',),  ('Female', 'Female'), ('Others', 'Others'))
blood_type = (('A', 'A'), ('A+', 'A+'), ('A-', 'A-'), ('B', 'B'),
              ('B+', 'B+'), ('B-', 'B-'), ('O', 'O'), ('O+', 'O+'), ('O-', 'O-'),)
consultation_type = (('', ''),
                     ('Online Consultation', 'Online Consultation'),
                     ('Face-Face Consultation', 'Face-Face Consultation'))
insurance = (('NHIF', 'NHIF'),
             ('Denver_Insurance', 'Denver_Insurance'),
             ('My_Doc', 'My_Doc'))

payment_mode = (('M-Pesa', 'M-Pesa'),
                ('Cash', 'Cash'),
                ('Credit Card', 'Credit Card'))


class Patient(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=60)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices=gender, default='Male')
    email = models.EmailField(blank=True)
    contact = models.IntegerField()
    birth_date = models.DateField(default=django.utils.timezone.now)
    languages = models.CharField(max_length=100, default='English')
    residence = models.CharField(max_length=100, default='Nairobi/Juja')
    blood_type = models.CharField(max_length=5, choices=blood_type, default='O')
    health_insurance = models.CharField(max_length=100, choices=insurance, blank=True, default='NHIF')
    height_cm = models.FloatField(default=130)
    weight_kg = models.FloatField(default=65)
    last_check = models.DateField(blank=True, default=django.utils.timezone.now)
    next_check = models.DateField(blank=True, default=django.utils.timezone.now)

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


class LabTechnician(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(default='enrc.jpg', upload_to='profile_pics', blank=True)
    bio = models.TextField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class LabReport(models.Model):
    tech_name = models.ForeignKey(LabTechnician, on_delete=models.PROTECT)
    user = models.ForeignKey(User, help_text='To which patient tests belong', null=True, on_delete=models.CASCADE, related_name="reds")
    tests = models.TextField()
    results = models.TextField()


class Clinician(models.Model):
    c_name = models.CharField(max_length=60)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)

    def __str__(self):
        return self.c_name


class Medrecs(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="meds")
    title = models.CharField(max_length=60, null=True)
    doctor = models.ForeignKey('Doctors.Doctor', null=True, on_delete=models.PROTECT)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, null=True)
    meds = models.TextField()

    def __str__(self):
        return self.title


class Appointment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="recrds")
    doc = models.ForeignKey('Doctors.Doctor', null=True, on_delete=models.PROTECT, related_name="dcts")
    name = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True, null=True)
    subject = models.CharField(max_length=60, null=True)
    number = models.IntegerField()
    location = models.CharField(max_length=60, null=True, default="Juja")
    email = models.EmailField()
    message = models.TextField()
    waiting_status = models.BooleanField(default=True)

    @property
    def is_waiting(self):
        return bool(self.waiting_status)

    def __unicode__(self):
        return self.user

    def __str__(self):
        return self.name + 'Subject:-' + self.subject


class UserAppointment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="recds")
    patient_name = models.CharField(max_length=60, null=True, help_text="The user selected above names';'")
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    consultation_type = models.CharField(max_length=30, blank=True, choices=consultation_type, default='No consultation')
    explanation = models.TextField(max_length=100, null=True)
    date = models.DateTimeField(help_text="Date of scheduled appointment")
    location = models.CharField(max_length=30, null=True)
    reason = models.TextField()

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
    to = models.ForeignKey(User, null=True, help_text='To which patient message belongs to', on_delete=models.CASCADE, related_name="record")
    clinician = models.ForeignKey(Clinician, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.subject


class Recept(models.Model):
    date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='To which Receipt belongs to', related_name="recpts")
    patient_name = models.CharField(max_length=100)
    amount_payed = models.CharField(max_length=300)
    payment_mode = models.CharField(max_length=30, choices=payment_mode)
    payed_for = models.CharField(max_length=300)

    def __str__(self):
        return self.patient_name
