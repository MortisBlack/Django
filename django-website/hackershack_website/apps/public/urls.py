from django.urls import path

from . import views

# Basicamente con esto digo que quiero que todas las URLS tengan el prefijo "public"
app_name = "public"
urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
]
