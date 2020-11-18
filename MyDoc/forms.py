from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from . models import *


"""class RegisterForm(forms.ModelForm):
    name = forms.CharField(max_length=60)
    gender = forms.CharField(max_length=60)
    email = forms.EmailField()
    number = forms.NumberInput()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User """


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ('username', 'image', 'age', 'gender', 'email', 'contact', 'blood_type')


class UserUpdate(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput)

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['image', 'age', 'contact']


class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=60)
    id_number = forms.CharField(max_length=60)
    number = forms.NumberInput()
    email = forms.EmailField()
    message = forms.Textarea()
    image = forms.FileField()

    class Meta:
        model = Appointment
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


