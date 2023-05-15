from django.contrib import admin
from . import models
# Register your models here.
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "dni")
    search_fields = ("apellido", "dni")
    list_filter = ("apellido", "dni")

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "stock_actual")
    search_fields = ("nombre", "precio", "stock_actual")
    list_filter = ("nombre", "precio", "stock_actual")

admin.site.register(models.Proveedor, ProveedorAdmin)
admin.site.register(models.Producto, ProductoAdmin)