from django import forms
from django.contrib.auth.forms import UserCreationForm

from . models import *


class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ('username', 'image', 'age', 'gender', 'email', 'contact', 'blood_type',
                  'residence', 'birth_date', 'height_cm', 'weight_kg', 'languages', 'health_insurance')


class UserUpdate(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['image', 'age', 'contact', 'languages', 'height_cm', 'weight_kg']


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['user', 'doc', 'name', 'subject', 'number', 'location', 'email', 'message']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
