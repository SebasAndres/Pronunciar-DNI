from django.urls import path
from pronunciar_dni_app import views

urlpatterns = [
    path("", views.home),
    path("home", views.home),
    path("result/<dni>", views.result_page),
    path("about", views.about),
    path("contact", views.contact)
]