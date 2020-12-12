from django.contrib import admin
from . models import Patientss, Doctor
from MyDoc.models import Appointment

# Register your models here.


class PatientInline(admin.TabularInline):
    model = Patientss
    extra = 0


class AppointmentsInline(admin.StackedInline):
    model = Appointment
    extra = 0


class DoctorAdmn(admin.ModelAdmin):
    inlines = [PatientInline, AppointmentsInline]


admin.site.register(Doctor, DoctorAdmn)
admin.site.register(Appointment)

