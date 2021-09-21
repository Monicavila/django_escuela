# django_escuela

Crear una aplicación para estudiantes que contenga un modelo Estudiante, una vista para listar los estudiantes en la base de datos y poder acceder al detalle de cada estudiante. Además crear un modelo para Clase, y una vista para poder ver la lista de clases disponibles.

PARA COMENZAR

- Genera tu SECRET_KEY, ejecuta:
    python generator_django.py

Abre en la carpeta Biblioteca Settings.py, linea 23 y pega tu SECRET_KEY entre las ''.

- Crea un superusuario, ejecuta:

   python manage.py createsuperuser

Ingresa un Username, email adress y un password

Abre el siguinete link para ingresar a la app.

http://127.0.0.1:8000/admin/

# URLS y Endpoints

Request Method: 	GET
Request URL: 	http://127.0.0.1:8000/

Using the URLconf defined in biblioteca.urls, Django tried these URL patterns, in this order:

    admin/
    alumnos/
    clases/
    facultades/
    profesores/
    api-auth
