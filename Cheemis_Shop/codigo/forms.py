#En esta clase se configuraran los formularios y sus campos para el crud.
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Categoria, Producto

#Clase de contiene los campos del formulario de los productos.}
class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields=['codigo','nombre','precios','descripcion','imagen','categoria']
        labels = {
            'codigo' : "Codigo",
            'nombre' : "Nombre",
            'descripcion' : "Descripcion",
            'precios' : "Precios",
            'imagen': "Imagen",
            'categoria':"Categoria"
        }
        widgets={
            'codigo' : forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese un codigo de producto',
                    'class' : 'form-control',
                    'id' : 'codigo'
                }
            ),
            'nombre':forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese un nombre del producto',
                    'class' : 'form-control',
                    'id' : 'nombre'
                }
            ),
            'descripcion':forms.Textarea(
                attrs={
                    'placeholder' : 'Ingrese una descripcion del producto',
                    'class' : 'form-control',
                    'id' : 'descripcion'
                }
            ),

            'categoria':forms.Select(
                attrs={
                    'class' : 'form-control',
                    'id' : 'categoria'
                }
            
            ),
            'imagen':forms.FileInput(
                attrs={
                    'class' : 'form-control',
                    'id' : 'imagen'
                }
            ),
            'precios':forms.NumberInput(
                attrs={
                    'placeholder' : 'Ingrese precio del prodcuto',
                    'class' : 'form-control',
                    'id' : 'precios'
                }
            ),
        }