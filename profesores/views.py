from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def vista_profesores(request):
    html = '<html><body>Hola desde Profesores</br><a href="http://127.0.0.1:8000/clases/">Clases</a></body></html>'
    return HttpResponse(html)