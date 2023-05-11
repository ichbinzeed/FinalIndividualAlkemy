from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, blank=False, null=False, verbose_name="Apellido")
    dni = models.IntegerField(blank=False, null=False, verbose_name="DNI")
    
    def __str__(self):
        return self.nombre
class Producto(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False, verbose_name="Nombre")
    precio = models.FloatField(blank=False, null=False, verbose_name="Precio")
    stock_actual = models.IntegerField(blank=False, null=False, verbose_name="Stock")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre