from django.shortcuts import render
from .models import Producto

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'app2/productos.html', {'productos': productos})

