# Proyecto Django con Bootstrap 5

Este proyecto proporciona una guía paso a paso para crear una aplicación Django utilizando **Bootstrap 5** para el diseño de interfaces.

---

## Tabla de Contenidos
- [Requisitos](#requisitos)
- [Configuración del Entorno](#configuración-del-entorno)
- [Pasos del Proyecto](#pasos-del-proyecto)
  - [Configuración Inicial](#configuración-inicial)
  - [Configuración del Proyecto](#configuración-del-proyecto)
  - [Creación de Vistas y Modelos](#creación-de-vistas-y-modelos)
  - [Integración de Bootstrap 5](#integración-de-bootstrap-5)
- [Credenciales Sugeridas](#credenciales-sugeridas)
- [Licencia](#licencia)

---

## Requisitos

- Python 3.9 o superior
- Django 4.0 o superior
- Bootstrap 5

---

## Configuración del Entorno

1. Crear el entorno virtual:
   ```bash
   python -m venv venv


## Activación del Entorno

2. Activar el entorno virtual:
    ### Windows
    ```bash
    venv\Scripts\activate

## Configuración Inicial
## Instalar Django y Guardar dependencias

3. Intalación Django
    ```bash
    pip install django

## Guardar las dependencias
4. Instalación dependencias
    ```bash
    pip freeze > requirements.txt

## Pasos del Proyecto
5. Crear el Proyecto
    ```bash
    django-admin startproject leccion3

6. Ingresar al directorio del Proyecto
    ```bash
    cd leccion3

7. Creamos la Aplicación app1
    ```bash
    python manage.py startapp app1

8. Creamos la Aplicación app2
    ```bash
    python manage.py startapp app2

## Configuración del Proyecto

9. Conectar el proyecto con la aplicación: Agregar 'app1' y 'app2' en la lista INSTALLED_APPS dentro del archivo leccion3/settings.py:
    ```bash
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app1',
    'app2',
    ]

10. en app1 creamos una Carpeta llamada templates creamos un archivo llamado index.html app1\templates\index.html

     ```bash
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>

    <body>
        <h1>Hola</h1>
    </body>

    </html>

11. en app1/views.py se configura el renderizado de la página index.html

    ```bash
    from django.shortcuts import render

    def index(request):
        return render(request, 'index.html')

12. Crear el archivo urls.py en app1 -> app1/urls

    ```bash
    from django.urls import path
    from app1 import views

    urlpatterns = [
        path('',views.index, name='index'),
    ]

13. Leccion3/urls, le damos la ruta para que conozca app1.urls

    ```bash
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('app1/',include('app1.urls')),
    
    ]

14. colocamos los siguientes comandos
    
    ```bash
    python manage.py makemigrations
    python manage.py migrate

15. Hacemos Correr en el Servidor nuestra Aplicación

    ```bash
    python manage.py runserver

16. Comprobamos en las paginas las rutas http://127.0.0.1:8000/app1/

17. Generamos la carpeta templates en la app2 y creamos el archivo productos.html
    ```bash
    <!DOCTYPE html>
    <html>

    <head>
        <title>Lista de Productos</title>
    </head>

    <body>
        <h1>Productos Disponibles</h1>
        <ul>
            {% for producto in productos %}
            <li>
                <strong>{{ producto.nombre }}</strong> - ${{ producto.precio }}<br>
                {{ producto.descripcion }}
            </li>
            {% endfor %}
        </ul>
    </body>

    </html>
18. en la leccion3/urls.py incluimos el path('app2/', include('app2.urls))
    
    ```bash
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('app1/',include('app1.urls')),
        path('app2/',include('app2.urls')),
    ]
19. en app2 creo un archivo urls.py
    ```bash
    from django.urls import path
    from app2 import views


    urlpatterns = [
        path('',views.productos, name='producto'),
    ]

20. Creamos el modelo en app2/models.py

    ```bash
    from django.db import models

    class Producto(models.Model):
        nombre = models.CharField(max_length=100)
        precio = models.DecimalField(max_digits=10, decimal_places=2)
        descripcion = models.TextField()

        def __str__(self):
            return self.nombre

21. Configuramos la vista y agregamos el modelo en app2/views.py

    ```bash
    from django.shortcuts import render
    from .models import Producto

    def productos(request):
        productos = Producto.objects.all()
        return render(request, 'productos.html', {'productos': productos})

22. Escribimos comandos de migracion a la base de datos

    ```bash
    python manage.py makemigrations
    python manage.py migrate

23. Vamos a Cargar datos en la Bases de Datos
    ```bash
    python manage.py shell


from app2.models import Producto
    
# Crear productos
Producto.objects.create(nombre="Mouse", precio=25.99, descripcion="Mouse inalámbrico")
Producto.objects.create(nombre="Teclado", precio=45.00, descripcion="Teclado mecánico")

# Verificar que los datos se insertaron correctamente
productos = Producto.objects.all()
for producto in productos:
    print(producto.nombre, producto.precio, producto.descripcion)

exit()
    


