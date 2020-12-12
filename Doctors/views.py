from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from .forms import *
from .models import Patientss, Doctor
from MyDoc.models import Patient, Appointment

from django.contrib.auth import login, authenticate, logout, admin


def indexview(request):
    if request.user.is_authenticated:
        dcts = Appointment.objects.all().filter(doc__doctor_name=request.user, waiting_status=True)
        context = {
            'dcts': dcts
            }
        return render(request, 'Doctors/index.html', context)
    else:
        return redirect('MyDoc:login_admn')


@login_required(login_url='MyDoc:login_admn')
def my_dct(request):
    if request.user.is_authenticated:
        dcts = Appointment.objects.all().filter(doc=request.user)
        return render(request, 'Doctors/index.html', {'dcts': dcts})
    else:
        return redirect('MyDoc:login_admn')


@login_required(login_url='Doctors:login_admn')
def all_patients(request):
    patient = Patient.objects.all()
    context = {
        'patient': patient
    }
    return render(request, 'Doctors/all_patients.html', context)


def login_admn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        dct = authenticate(username=username, password=password)
        if dct is not None:
            if dct.is_active and dct.doctor:
                login(request, dct)
                return redirect('Doctors:index')
            elif dct is not dct.doctor:
                messages.error(request, 'Not a Doctor!!...')
                return redirect('Doctors:login_admn')
        else:
            messages.error(request, 'Invalid Login! ... Try Again')
            return redirect('Doctors:login_admn')
    return render(request, 'Doctors/signDct.html')


def medrecs(request):
    form = MedForm(request.POST or None)
    if form.is_valid():
        appnt = form.save(commit=False)
        appnt.title = request.POST['title']
        appnt.meds = request.POST['meds']
        appnt.save()
        messages.success(request, f'Medical Records Added.')
    form = MedForm()
    return render(request, 'Doctors/medrecs.html', {'form': form})


def dct_appnt(request):
    form = UserAppointmentForm(request.POST or None)
    if form.is_valid():
        appnt = form.save(commit=False)
        appnt.patient_name = request.POST['patient_name']
        appnt.consultation_type = request.POST['consultation_type']
        appnt.explanation = request.POST['explanation']
        appnt.date = request.POST['date']
        appnt.location = request.POST['location']
        appnt.reason = request.POST['reason']
        appnt.save()
        messages.success(request, f'Appointment to { appnt.patient } has been scheduled')
    form = UserAppointmentForm()
    return render(request, 'Doctors/schedule_appointment.html', {'form': form})


class PatientCreateView(CreateView):
    model = Patient
    fields = ["doctor", "patient_name"]
    success_url = reverse_lazy("Doctors:index")


class PatientDetailView(DetailView):
    model = Patient
    template_name = "Doctors/patient_detail.html"


class PatientUpdateView(UpdateView):
    model = Patient
    fields = ["patient_name"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("Doctors:index")


class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy("Doctors:index")


class DoctorDetailView(CreateView):
    model = Doctor
    template_name = "Doctors/doctor_detail.html"

