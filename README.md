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
