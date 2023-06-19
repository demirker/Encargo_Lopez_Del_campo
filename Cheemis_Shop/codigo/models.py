from django.db import models
from tabnanny import verbose

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de Categoria")
    nombreCategoria= models.CharField(max_length=50, blank=True, verbose_name="Nombre de Categoria")
    
    def __str__(self):
        return self.nombreCategoria 
    
class Producto(models.Model):
    codigo= models.CharField(primary_key=True, max_length=8, verbose_name="Codigo Producto")
    nombre=models.CharField(max_length=50, blank=True, verbose_name="Nombre Producto")
    descripcion=models.TextField(max_length=200, blank=True, verbose_name="Descripcion del Producto")
    precios=models.IntegerField( blank=True, verbose_name="Precio del producto")
    imagen=models.ImageField(upload_to='imagenes', null=True ,verbose_name="Imagen")
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    
    def __str__(self):
        return self.nombre