from django.shortcuts import render, redirect
# Para crear usuario de la web
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Para proteger las vistas:
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html', {'user': request.user})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # Esto crea el nuevo usuario
            return redirect('login') # Redirige a la página de login
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index') # Redirige a la página principal
        else:
            # Manejo de error de autenticación
            pass
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

# Crear vista protegida
@login_required(login_url='login')
def vista_protegida(request):
    if request.user.is_authenticated:
        return render(request, 'vista_protegida.html', {'user': request.user})
    else:
        return redirect('login') # Redirige a la página de login si no está autenticado