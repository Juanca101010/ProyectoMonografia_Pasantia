from django.shortcuts import render, redirect
from multiprocessing import context
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from app.models import Cliente, Correo, Documentacion, Tarea, Usuario, VPN 


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
def smsEmail(request):

    return render(request, 'app/smsEmail.html')


def help(request):

    return render(request, 'app/help.html')
def icareplus(request):

    return render(request, 'app/icareplus.html')
def netcare(request):

    return render(request, 'app/netcare.html')
def onebox(request):

    return render(request, 'app/onebox.html')
def profile(request):

    return render(request, 'app/profile.html')
def vpnaccess(request):

    return render(request, 'app/vpnaccess.html')