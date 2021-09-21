from django.urls import path

from alumnos.views import vista_alumnos, detalle_alumno

app_name = 'alumnos'
urlpatterns = [
    path('', vista_alumnos, name='list'),
    path('<int:alumno_id>/', detalle_alumno, name="detail")
]
