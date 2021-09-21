##from django.http import HttpResponse
from django.shortcuts import render, redirect

from alumnos.models import Alumno

# Create your views here.


def vista_alumnos(request):
##    fecha = '2021-03-27'
##    html = '<html><body>Hola desde Alumnos</body></html>'
##    return HttpResponse(html)
    if request.method == 'GET':
        alumnos = Alumno.objects.all()
        contexto = {
            'alumnos_lista': alumnos
        }
        return render(request, 'alumnos/list.html', contexto)

    if request.method == 'POST':
        print('Agregar un nuevo alumno')
        nuevo_alumno = Alumno.objects.create(
            nombre=request.POST['nombre'],
            apellido =request.POST['apellido'],
            carrera=request.POST['carrera'],
            correo=request.POST['correo']
        )
        alumnos = Alumno.objects.all()
        contexto = {
            'alumnos_lista': alumnos
        }
        return render(request, 'alumnos/list.html', contexto)

    if request.method == 'POST':
        alumno.delete()
        return redirect('alumnos:list')


def detalle_alumno(request, alumno_id):
    alumno = Alumno.objects.get(id=alumno_id)
    contexto = {
        'alumno': alumno
    }
    return render(request, 'alumnos/detail.html', contexto)
