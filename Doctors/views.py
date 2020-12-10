from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from .forms import *
from .models import *

from django.contrib.auth import login, authenticate, logout, admin


class IndexView(ListView):
    context_object_name = "patient_list"
    template_name = "Doctors/index.html"

    def get_queryset(self):
        return Patient.objects.filter(waiting_status=True)


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

