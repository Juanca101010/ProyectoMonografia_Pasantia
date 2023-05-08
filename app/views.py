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

    lista = Tarea.objects.all()
    print(lista)
    contexto ={
        'tareas':lista,
    }

    return render(request, 'app/dashboardhw.html',contexto)

def dashboardhws(request):

    lista = Tarea.objects.all()
    print(lista)
    contexto ={
        'tareas':lista,
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
    contexto ={
    'c':clientes,
    }

    owners=User.objects.all()
    contexto ={
    'u':owners,
    }
    return render(request, 'app/netcare.html',contexto)

def crear_tarea(request):
    try:
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        fecha_vencimiento = request.POST['fecha_vencimiento']
        Cliente = request.POST['Cliente']
        owner = request.POST['owner']

        id_usuario=request.user.id

        t = Tarea()
        t.titulo=titulo
        t.descripcion = descripcion
        t.progreso = 0
        t.fecha_vencimiento = fecha_vencimiento
        t.contacto_cliente=Cliente
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