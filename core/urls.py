from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .schema import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("task1/api/v1/", include('apps.task1.urls')),
    path('task2/api/v1/', include('apps.task2.urls')),
    path("task3/api/v1/", include('apps.task3.urls')),
    path("task4/api/v1/", include('apps.task4.urls'))
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
