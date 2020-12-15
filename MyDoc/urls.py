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
    path('patient', views.patient, name='patient'),
    path('(?<pat_id>[0-9]+)/', views.detail, name='detail'),
    path('(?<pat_id>[0-9]+)/med_detal', views.med_detal, name='med_detal'),

    path('profile_update', views.profile_update, name='profile_update'),
    path('(?<pat_id>[0-9]+)/delete_pat', views.delete_pat, name='delete_pat'),
    path('(?<mess_id>[0-9]+)/delete_mess', views.delete_mess, name='delete_mess'),

    path('contact', views.contact, name='contact'),
    path('message', views.message, name='message'),
    path('recept', views.recept, name='recept'),
    path('doctors', views.doctors, name='doctors'),
    path('doc_ndex', views.doc_ndex, name='doc_ndex'),

    path('login_patient', views.login_patient, name='login_patient'),
    path('login_admn', views.login_admn, name='login_admn'),
    path('logout_patient', views.logout_patient, name='logout_patient'),
    path('register/', views.register_patient, name='register'),


    path('appointment', views.appointment, name='appointment'),
    path('consultation', views.consultation, name='consultation'),
    path('(?<appointment_id>[0-9]+)/appnt_detail', views.appnt_detail, name='appnt_detail'),
    path('u_appointment', views.u_appointment, name='u_appointment'),
    path('(?<appointment_id>[0-9]+)/delete_appnt', views.delete_appnt, name='delete_appnt'),
    path('(?<appointment_id>[0-9]+)/delete_appnt_detal', views.delete_appnt_detal, name='delete_appnt_detal'),

    path('my_profile', views.my_profile, name='my_profile'),
    path('patient_profile', views.patient_profile, name='patient_profile'),
    path('medrecs', views.medrecs, name='medrecs'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)