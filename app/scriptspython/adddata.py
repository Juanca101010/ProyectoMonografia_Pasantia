import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nombre_de_tu_app.settings')
import django
django.setup()

from django.contrib.auth.models import User
from app.models import Cliente, Tarea

# Obtener el cliente y el propietario
cliente = Cliente.objects.get(id=3)
propietario = User.objects.get(id=1)

# Crear una nueva tarea
tarea = Tarea.objects.create(
    titulo='titulo de la tarea 2',
    descripcion='descripcion de la tarea nuemero 2',
    progreso=0,
    fecha_vencimiento='2024-08-08',
    contacto_cliente=cliente,
    owner=propietario
)

# Guardar el first_name del propietario en el campo owner
tarea.owner_name = tarea.owner.first_name
tarea.save()

