from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCliente/', views.registrarCliente),
    path('edicionCliente/<codigo>', views.edicionCliente),
    path('editarCliente/', views.editarCliente),
    path('eliminarCliente/<codigo>', views.eliminarCliente)
]