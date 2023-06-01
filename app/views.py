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

def restorepass(request):

    return render(request, 'app/restorepass.html')

def autenticar(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            if user.is_superuser:
                return redirect('app:dashboardhws')  # Redirige a la página de inicio de sesión para superusuarios
            else:
                return redirect('app:dashboardhw')  # Redirige a la página de inicio de sesión para usuarios no superadministradores
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
    tareas = Tarea.objects.all()
    contexto = {'tareas': []}

    for tarea in tareas:
        cliente = Cliente.objects.get(id=tarea.contacto_cliente_id)
        tarea.cliente = cliente.nombre+'-'+cliente.contacto  # Agregar el atributo "cliente" a la tarea
        contexto['tareas'].append(tarea)

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
    tareas = Tarea.objects.all()
    contexto ={
    'tareas': [],
    'c':clientes,
    'u':owners,
    }

    for tarea in tareas:
        cliente = Cliente.objects.get(id=tarea.contacto_cliente_id)
        tarea.cliente = cliente.nombre+'-'+cliente.contacto  # Agregar el atributo "cliente" a la tarea
        contexto['tareas'].append(tarea)

    return render(request, 'app/netcare.html',contexto)


def ADMIN(request):
    try:
        usern = request.POST['usern']
        name1 = request.POST['name1']
        name2 = request.POST['name2']
        email = request.POST['email']
        password = request.POST['pass']
        superu = bool(int(request.POST['superu']))  # Convert superu to boolean

        u = User()
        u.first_name = name1
        u.last_name = name2
        u.email = email
        u.is_superuser = superu
        u.set_password(password)  # Use set_password to securely store the password
        u.username = usern
        u.save()

        return redirect('app:ADMIN')
    except Exception as e:
        print(e)
    return render(request, 'app/ADMIN.html')


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