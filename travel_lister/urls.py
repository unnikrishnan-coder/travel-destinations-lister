from django.urls import path

from . import views
app_name = "travel_lister"
urlpatterns = [
    path("", views.index, name="index"),
    path("/generate", views.generate, name="generate"),
    path("/download_file/<str:filename>", views.download_file, name="download_file"),
]