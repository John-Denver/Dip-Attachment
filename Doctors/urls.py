from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url


app_name = 'Doctors'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('doctor/<int:pk>/', views.DoctorDetailView.as_view(), name='doctor_detail'),
    path('patient/<int:pk>/', views.PatientDetailView.as_view(), name='patient_detail'),
    path('patient/<int:pk>/edit', views.PatientUpdateView.as_view(), name='patient_update'),
    path('patient/create', views.PatientCreateView.as_view(), name='patient_create'),
    path('patient/<int:pk>/delete', views.PatientDeleteView.as_view(), name='patient_delete'),

    ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
