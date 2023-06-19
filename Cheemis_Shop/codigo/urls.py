from django.urls import path

from codigo.views import inicio, informacion,catalogo_productos,agregar_producto,eliminar,modificar

urlpatterns=[
    path('', inicio, name='inicio'), #comillas simples vacias es para que sea la pagina inicial
    path('informacion/', informacion, name='informacion'),
    path('catalogo_productos/', catalogo_productos, name='catalogo_productos'),
    path('agregar_producto/', agregar_producto, name="agregar_producto"),
    path('eliminar/<codigo>', eliminar, name="eliminar"),
    path('modificar/<codigo>', modificar, name="modificar"),
    
]