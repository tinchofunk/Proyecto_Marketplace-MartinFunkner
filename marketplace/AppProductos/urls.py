from django.urls import path
from AppProductos import views
urlpatterns = [
    path("",views.inicio,name="Inicio"),
    path('productos/', views.productos,name="productos"),
    path('cliente/', views.cliente,name="cliente"),
    path('stock/', views.stock,name="stock"),
    path("busquedaproducto/",views.buscarproducto),
    path("buscar/",views.buscar)
]