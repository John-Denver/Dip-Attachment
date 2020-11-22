from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

from django.contrib.auth.decorators import login_required
from django.contrib import admin
admin.autodiscover()

admin.site.site_header = "HOSPITAL ADMINISTRATION"
admin.site.index_title = "Denver Health-Care E-Hospital"

admin.site.login = login_required(admin.site.login)

urlpatterns = [
    path('admin/', admin.site.urls),
    url('health/', include('MyDoc.urls')),
]


if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
