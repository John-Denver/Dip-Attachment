from django.contrib import admin
from . models import *

# Register your models here.


class PatientInline(admin.TabularInline):
    model = Patient
    extra = 0


class DoctorAdmn(admin.ModelAdmin):
    inlines = [PatientInline]


admin.site.register(Doctor, DoctorAdmn)
