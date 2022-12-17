from django.contrib import admin
from django.urls import path

from validation.views import verify

urlpatterns = [
    path("admin/", admin.site.urls),
    path("verify/", verify),
]
