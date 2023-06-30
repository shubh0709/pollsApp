from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("polls/", include("app_polls.urls")),
    path("admin/", admin.site.urls),
]