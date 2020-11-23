from django.conf.urls import url
from . import views
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url


app_name = 'the_user'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<appointment_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<consultation_id>[0-9]+)/isdoctor/$', views.isdoctor, name='isdoctor'),
    url(r'^consultations/(?P<filter_by>[a-zA_Z]+)/$', views.consultations, name='consultations'),
    url(r'^create_appointment/$', views.create_appointment, name='create_appointment'),
    url(r'^(?P<appointment_id>[0-9]+)/create_consultation/$', views.create_consultation, name='create_consultation'),
    url(r'^(?P<appointment_id>[0-9]+)/delete_consultation/(?P<consultation_id>[0-9]+)/$', views.delete_consultation, name='delete_consultation'),
    url(r'^(?P<appointment_id>[0-9]+)/favorite_appointment/$', views.favorite_appointment, name='favorite_appointment'),
    url(r'^(?P<appointment_id>[0-9]+)/delete_appointment/$', views.delete_appointment, name='delete_appointment'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
