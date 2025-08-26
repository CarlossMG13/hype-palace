from django.shortcuts import render
from .models import Producto

# Create your views here.
def index(request):
    # Obtiene todos los productos de la base de datos donde is_active es True
    productos = Producto.objects.filter(is_active=True)
    
    # Prepara el "contexto" con la lista de productos
    context = {
        'productos': productos
    }
    
    # Renderiza la plantilla y le pasa los datos
    return render(request, 'store/index.html', context)