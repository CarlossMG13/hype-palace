from django.urls import path
from . import views # Importa todas las vistas de la app

urlpatterns = [
    # 'path' con una cadena vacía ('') para la URL de inicio,
    # que ejecutará la vista 'index' y le dará el nombre 'index'.
    path('', views.index, name='index'),
]
