from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Producto,Categoria
from .forms import ProductoForm

# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def informacion(request):
    return render(request,'informacion.html')

def catalogo_productos(request):
    productos=Producto.objects.all()
    datos={'productos':productos}
    return render(request,'Catalogo_productos.html',datos)

@login_required
def agregar_producto(request):
    if request.method=="POST":
        prodcutoform =ProductoForm(request.POST, request.FILES) 
        if prodcutoform.is_valid():
            prodcutoform.save() 
            return redirect ('catalogo_productos')
    else:
        prodcutoform=ProductoForm()
    return render(request, 'agregar_producto.html', {'productoform' : prodcutoform})

@login_required
def eliminar(request,codigo):
    productoEliminado=Producto.objects.get(codigo=codigo)
    productoEliminado.delete()
    return redirect('catalogo_productos')

@login_required
def modificar(request,codigo):
    productoModificado=Producto.objects.get(codigo=codigo)
    datos={
        'form':ProductoForm(instance=productoModificado)
    }
    if request.method=="POST":
        formulario = ProductoForm(request.POST,request.FILES, instance= productoModificado)
        if formulario.is_valid():
            formulario.save()
            return redirect('catalogo_productos')
    return render(request,'modificar_producto.html',datos)