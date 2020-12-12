from django import forms
from django.contrib.auth.forms import UserCreationForm

from . models import *
from MyDoc.models import Medrecs, UserAppointment


class MedForm(forms.ModelForm):

    class Meta:
        model = Medrecs
        fields = '__all__'


class UserAppointmentForm(forms.ModelForm):

    class Meta:
        model = UserAppointment
        fields = '__all__'

