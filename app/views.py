from django.shortcuts import render, redirect
from multiprocessing import context
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from app.models import Cliente, Correo, Documentacion, Tarea, Usuario, VPN 
from django.contrib.auth.models import User



#-------------------------------------------
def loginhw(request):

    return render(request, 'app/loginhw.html')

def autenticar(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            print(username)
            print(password)
            if request.user.is_superuser:
                return redirect('app:dashboardhw')
            else:
                return redirect('app:dashboardhw')
        else:
            # Si el usuario no existe, devuelve una respuesta con el mensaje de error.
            return render(request, "app/loginhw.html", {'error_message': 'Usuario o contraseña incorrecta'})
    else:
        return render(request, "app/loginhw.html")


def view_logout(request):
  # Cierra la sesión del usuario
  logout(request)
  # Redirecciona la página de login
  return redirect('app:ingresar')
#--------------------------------------------
def dashboardhw(request):
    tareas = Tarea.objects.all()
    contexto = {'tareas': []}

    for tarea in tareas:
        cliente = Cliente.objects.get(id=tarea.contacto_cliente_id)
        tarea.cliente = cliente.nombre+'-'+cliente.contacto  # Agregar el atributo "cliente" a la tarea
        contexto['tareas'].append(tarea)

    return render(request, 'app/dashboardhw.html', contexto)


def dashboardhws(request):
    cl=Cliente.objects.all()
    lista = Tarea.objects.all()

    cl = Cliente.objects.filter(id=lista.contacto.cliente)

    print(lista)
    contexto ={
        'tareas':lista,
        'clientes':cl,
    }

    return render(request, 'app/dashboardhws.html',contexto)

def smsEmail(request):

    return render(request, 'app/smsEmail.html')


def help(request):

    return render(request, 'app/help.html')
def icareplus(request):

    return render(request, 'app/icareplus.html')
def netcare(request):
    clientes=Cliente.objects.all()
    owners=User.objects.all()
    contexto ={
    'c':clientes,
    'u':owners,
    }
    return render(request, 'app/netcare.html',contexto)

def crear_tarea(request):
    try:
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        fecha_vencimiento = request.POST['fecha_vencimiento']
        cl = request.POST['cliente']
        ow = request.POST['owner']

        cliente= Cliente.objects.get(id=cl)

        owner= User.objects.get(id=ow)

        t = Tarea()
        t.titulo=titulo
        t.descripcion = descripcion
        t.progreso = 0
        t.fecha_vencimiento = fecha_vencimiento
        t.contacto_cliente=cliente
        t.owner=owner
        t.save()

        return redirect('app:dashboardhw')
    except Exception as e:
        print(e)
        return render(request,'app/dashboardhw.html')

def onebox(request):

    return render(request, 'app/onebox.html')
def profile(request):

    return render(request, 'app/profile.html')
def vpnaccess(request):

    return render(request, 'app/vpnaccess.html')


def ejecutartarea(request):

    return render(request, 'app/ejecutartarea.html')