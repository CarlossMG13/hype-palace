from django.db import models

# Create your models here.

# Producto Model
class Producto(models.Model):
    # Atributos
    
    nombre = models.CharField(max_length = 255) # Nombre producto
    precio = models.DecimalField(max_digits = 8, decimal_places = 2) # Precio producto
    descripcion = models.TextField() # Descripcion producto
    categoria = models.CharField(max_length = 25) # Categoria producto (sneakers, apparel, coleccionables, accesorios)
    stock = models.IntegerField() # Cantidad en stock del mismo producto
    is_active = models.BooleanField() # Verifica estado del producto en el stock (disponible, no disponible)
    
    etiquetas = models.ManyToManyField('Etiqueta') # Relacion de etiquetas muchos a muchos
    
    # Funcion para que aparezca el nombre del producto en la tabla Productos
    def __str__(self):
        return self.nombre
    
    
# Imagen Model -> Producto
class Imagen(models.Model):
    #Atributos
    img_producto = models.ImageField() # Imagen del producto  
    img_descripcion = models.CharField(max_length = 150) # Descripcion de la imagen (SEO/accesibilidad)
    img_principal = models.BooleanField()  # Imagen principal del producto
    
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE) # Relacion a modelo Producto
    
# Etiqueta Model -> Producto
class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50) # Agrega un nombre para la etiqueta
    
    def __str__(self):
        return self.nombre 
    

    
    
    