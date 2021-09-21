from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def vista_clases(request):
    html = '<html><body>Hola desde Clases</body></html>'
    return HttpResponse(html)
