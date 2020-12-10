from django.contrib import admin
from . models import *


# Register your models here.

admin.site.register(Patient)
admin.site.register(Contact)
admin.site.register(Appointment)

admin.site.register(Clinician)
admin.site.register(Department)
admin.site.register(Medrecs)
admin.site.register(Message)
admin.site.register(Doctor)
admin.site.register(Recept)
admin.site.register(LabTechnician)
admin.site.register(LabReport)
admin.site.register(UserAppointment)
