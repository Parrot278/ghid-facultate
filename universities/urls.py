from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.ecran_principal, name="ecranprincipal"),
    path("facultatiromania/", views.facultati_romania, name = "facultatiromania"),
    path("catalogfacultati/", views.catalog_facultati, name = "catalogfacultati"),
    path("chestionar/", views.chestionar, name = "chestionar"),
    path("bibliografie/", views.bibliografie, name = "bibliografie"),
    path("cvmeniu/", views.cv_meniu, name = "cvmeniu"),
    path("<int:facultate_id>/detaliifacultate/", views.detalii_facultate, name="detaliifacultate"),
    path('', views.feedback_form, name='form'),
    path('admin/', views.FeedbackListView.as_view(), name='admin'),
    path('feedback/', include('feedback.urls', namespace='feedback')),
]
