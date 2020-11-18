from django.contrib import messages
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views import View
from django.views.generic import CreateView

from .forms import *
from .models import *

from django.contrib.auth import login, authenticate, logout

# Create your views here.

def index(request):
    contact = Contact.objects.all()

    appointment = Appointment.objects.all()

    context = {
        'contact': contact,

        'appointment': appointment,
    }

    return render(request, 'MyDoc/index.html', context)


class Appointment(View):
    @staticmethod
    def get(request, *args, **kwargs):
        return render(request, 'MyDoc/appointment.html')

    def post(self, request, *args, **kwargs):
        form = AppointmentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            return redirect('MyDoc:index')
        appnt = form.save(commit=False)
        appnt.name = request.POST['name']
        appnt.id_number = request.POST['id_number']
        appnt.number = request.POST['number']
        appnt.email = request.POST['email']
        appnt.message = request.POST['message']
        appnt.image = request.FILES['image']
        appnt.save()
        form = AppointmentForm()

        return render(request, 'MyDoc/index.html', {'form': form})


"""
def appointment(request):
    form = AppointmentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        appnt = form.save(commit=False)
        appnt.name = request.POST['name']
        appnt.id_number = request.POST['id_number']
        appnt.number = request.POST['number']
        appnt.email = request.POST['email']
        appnt.message = request.POST['message']
        appnt.image = request.FILES['image']
        appnt.save()
    form = AppointmentForm()
    return render(request, 'MyDoc/appointment.html', {'form': form}) """


def doctors(request):
    return render(request, 'MyDoc/doctors.html')


def patient_profile(request, user):
    form = PatientForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.username = request.POST['username']
        user.image = request.POST['image']
        user.age = request.POST['age']
        user.gender = request.POST['gender']
        user.email = request.POST['email']
        user.contact = request.POST['contact']
        user.blood_type = request.POST['blood_type']
        user.user = request.user
        user.save()
        return render(request, 'MyDoc/my_profile.html', {'user': user})
    form = PatientForm()
    return render(request, 'MyDoc/profile_update.html', {'form': form})


def patient(request):
    form = PatientForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.username = request.POST['username']
        user.image = request.FILES['image']
        user.age = request.POST['age']
        user.gender = request.POST['gender']
        user.email = request.POST['email']
        user.contact = request.POST['contact']
        user.blood_type = request.POST['blood_type']
        user.user = request.user
        user.save()
    form = PatientForm()
    return render(request, 'MyDoc/patient.html', {'form': form})


def detail(request, pat_id):
    patient = get_object_or_404(Patient, pk=pat_id)
    return render(request, 'MyDoc/detail_pat.html', {'patient': patient})


def my_profile(request):
    meds = Medrecs.objects.all()
    if request.user.is_authenticated:
        return render(request, 'MyDoc/my_profile.html', {'meds': meds})
    else:
        return redirect('MyDoc:login_patient')


def profile_update(request):
    if request.method == 'POST':
        u_update = UserUpdate(request.POST, instance=request.user)
        p_update = ProfileUpdate(request.POST, request.FILES, instance=request.user.patient)
        if u_update.is_valid() and p_update.is_valid():
            u_update.save()
            p_update.save()
            messages.success(request, f'Your account has been Updated!')
            return redirect('MyDoc:my_profile')
    else:
        u_update = UserUpdate(instance=request.user)
        p_update = ProfileUpdate(instance=request.user.patient)
    context = {
        'u_update': u_update,
        'p_update': p_update
    }

    return render(request, 'MyDoc/my_profile.html', context)


def medrecs(request):
    meds = MedRecs.objects.all()
    return render(request, 'MyDoc/Department.html', {'meds': meds})


def all_patients(request):
    patient = Patient.objects.all()
    context = {
        'patient': patient
    }
    return render(request, 'MyDoc/all_patients.html', context)


def delete_pat(request, pat_id):
    patient = Patient.objects.get(pk=pat_id)
    patient.delete()
    patient = Patient.objects.all()
    return render(request, 'MyDoc/all_patients.html', {'patient': patient})


def register_patient(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password, first_name=first_name, last_name=last_name,
                            email=email)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('MyDoc:login_patient')
    return render(request, 'MyDoc/register.html', {'form': form})


def login_patient(request, self=None):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if user.patient:
                    login(request, user)
                    return redirect('MyDoc:my_profile')
            elif patient.DoesNotExist:
                return redirect('MyDoc:patient')

    return render(request, 'MyDoc/sign-in.html')


def logout_patient(request):
    logout(request)
    return redirect('MyDoc:login_patient')


def contact(request):
    form = ContactForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        mes = form.save(commit=False)
        mes.name = request.POST['name']
        mes.email = request.POST['email']
        mes.subject = request.POST['subject']
        mes.message = request.POST['message']
        mes.save()
    form = ContactForm()
    return render(request, 'MyDoc/contact.html', {'form': form})