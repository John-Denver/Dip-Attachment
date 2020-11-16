from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url


app_name = 'MyDoc'


urlpatterns = [
    path('', views.index, name='index'),
    path('all_patients', views.all_patients, name='all_patients'),
    path('(?<pat_id>[0-9]+)/', views.detail, name='detail'),
    path('patient_profile', views.patient_profile, name='patient_profile'),
    path('(?<pat_id>[0-9]+)/delete_pat', views.delete_pat, name='delete_pat'),

    path('contact', views.contact, name='contact'),
    path('doctors', views.doctors, name='doctors'),

    path('login_patient', views.login_patient, name='login_patient'),
    path('logout_patient', views.logout_patient, name='logout_patient'),
    path('register/', views.register_patient, name='register'),


    path('appointment', views.Appointment.as_view(), name='appointment'),
    path('my_profile', views.my_profile, name='my_profile'),
    path('patient_profile', views.patient_profile, name='patient_profile'),

    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
