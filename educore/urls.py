
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("students/", include("students.urls")),
    path("students/", include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


