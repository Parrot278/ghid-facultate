from django.urls import path
from . import views

urlpatterns = [
    path("", views.ecran_principal, name="ecranprincipal"),
    path("facultatiromania/", views.facultati_romania, name = "facultatiromania"),
    path("catalogfacultati/", views.catalog_facultati, name = "catalogfacultati"),
    path("chestionar/", views.chestionar, name = "chestionar"),
    path("bibliografie/", views.bibliografie, name = "bibliografie"),
    path("cvmeniu/", views.cv_meniu, name = "cvmeniu"),
]
