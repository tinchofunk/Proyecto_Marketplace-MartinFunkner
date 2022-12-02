from django.shortcuts import render
from django.http import HttpResponse

from AppProductos.models import Productos, Cliente, Stock
from django.core import serializers

from AppProductos.forms import ProductosFormulario
from AppProductos.forms import ClienteFormulario
from AppProductos.forms import StockFormulario

# Create your views here.


def buscar(request):
    categorias_views = request.GET['categorias']
    productos_todos = Productos.objects.filter(categorias=categorias_views)
    return render(request, "AppProductos/resultadoproducto.html", {"camada": categorias_views, "productos": productos_todos})


def buscarproducto(request):
    return render(request, "AppProductos/buscarproducto.html")


def inicio(request):
    return render(request, "AppProductos/inicio.html")


def productos(request):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = ProductosFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            productos = Productos(
                producto=informacion["producto"], categoria=informacion["categoria"])
            productos.save()
            return render(request, "AppProductos/inicio.html")
    else:
        miFormulario = ProductosFormulario()

    return render(request, "AppProductos/productos.html", {"miFormulario": miFormulario})


def cliente(request):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = ClienteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            print(informacion)
            usuario = Cliente(usuario=informacion["usuario"], fecha_alta=informacion["fecha_alta"])
            usuario.save()
            return render(request, "AppProductos/inicio.html")
    else:
        miFormulario = ClienteFormulario()

    return render(request, "AppProductos/cliente.html", {"miFormulario": miFormulario})


def stock(request):
    if request.method == "POST":
        # Aqui me llega la informacion del html
        miFormulario = StockFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            print(informacion)
            precio = Stock(precio=informacion["precio"], stock=informacion["stock"])
            precio.save()
            return render(request, "AppProductos/inicio.html")
    else:
        miFormulario = StockFormulario()

    return render(request, "AppProductos/stock.html", {"miFormulario": miFormulario})


def productosapi(request):
    productos_todos = Productos.objects.all()
    return HttpResponse(serializers.serialize("json", productos_todos))
