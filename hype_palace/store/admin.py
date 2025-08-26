from django.contrib import admin
from .models import Producto, Imagen, Etiqueta # Importa todos los modelos

# Register your models here.
admin.site.register(Producto)
admin.site.register(Imagen)
admin.site.register(Etiqueta)