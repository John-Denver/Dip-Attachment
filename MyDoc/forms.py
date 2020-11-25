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
                  'residence', 'birth_date', 'languages', 'health_insurance')


class UserUpdate(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['image', 'age', 'contact']


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
