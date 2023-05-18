import random
from app.models import Documentacion

def generarDatosAleatorios():
    nombres = ['doc_equipo1', 'doc_equipo2', 'doc_equipo3', 'doc_equipo4', 'doc_equipo5']
    nombres2 = ['verison1', 'verison2', 'verison3', 'verison4', 'verison5']
    nombres3 = ['cliente1', 'cliente2', 'cliente3', 'cliente4', 'cliente5']
    nombres4 = ['operador1', 'operador2', 'operador3', 'operador4', 'operador5']

    nombreAleatorio = random.choice(nombres)
    nombre2Aleatorio = random.choice(nombres2)
    archivos = random.choice(nombres3)
    archivos2 = random.choice(nombres4)
    tipoAleatorio = random.randint(0, 50)

    return {
        'nombre': nombreAleatorio + nombre2Aleatorio,
        'tipo': str(tipoAleatorio),
        'archivo': archivos + archivos2,
    }

def llenarBaseDeDatos():
    totalRegistros = 20

    for _ in range(totalRegistros):
        datos = generarDatosAleatorios()

        documentacion = Documentacion(
            nombre=datos['nombre'],
            tipo=datos['tipo'],
            archivo=datos['archivo']
        )

        documentacion.save()

        print('Registro insertado correctamente')

# Llenar la base de datos con datos aleatorios
llenarBaseDeDatos()
