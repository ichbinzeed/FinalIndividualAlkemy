from django.shortcuts import render, HttpResponse
from .forms import *
from django.contrib import messages
from .models import *

# Create your views here.
def agregarproveedor(request):    
    if request.method == "POST":
        proveedorForm = ProveedorForm(request.POST)
        if proveedorForm.is_valid():
            messages.info(request, 'Quedan 3 créditos en tu cuenta.')
            proveedorForm.save()            
        else:
            return HttpResponse("Hubo un error")
        
    proveedorForm = ProveedorForm()
    return render(request,"agregarproveedor.html",{"proveedorForm":proveedorForm})

def agregarproducto(request):
    if request.method == "POST":
        productoForm = ProductoForm(request.POST)
        if productoForm.is_valid():
            productoForm.save()            
        else:
            return HttpResponse("Hubo un error")        
    productoForm = ProductoForm()
    return render(request,"agregarproducto.html",{"productoForm":productoForm})

def listadoproveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, "listadoproveedores.html", {"proveedores":proveedores})

def listadoproductos(request):
    productos = Producto.objects.all()
    return render(request, "listadoproductos.html", {"productos":productos})