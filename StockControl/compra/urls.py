from django.urls import path
from . import views

urlpatterns = [
    path("agregarproveedor", views.agregarproveedor, name="agregarproveedor"),
    path("agregarproducto", views.agregarproducto, name="agregarproducto"),
    path("listadoproveedores", views.listadoproveedores, name="listadoproveedores"),
    path("listadoproductos", views.listadoproductos, name="listadoproductos")
]