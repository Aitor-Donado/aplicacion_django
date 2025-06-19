from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
from .forms import UsuarioForm
from .models import Material, Usuario, Prestamo


def hello(request):
    return HttpResponse(b"Hello World")

def agregar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'agregar_usuario.html', {'form': form})

from .models import Material
import uuid

def agregar_material(request):
    if request.method == "POST":
        codigo_inventario = uuid.uuid4().hex
        titulo = request.POST.get("titulo")
        tipo = request.POST["tipo"]
        autor = request.POST.get("autor") or None
        isbn = request.POST.get("isbn") or None
        numero_paginas = request.POST.get("numero_paginas")
        fecha_publicacion = request.POST.get("fecha_publicacion") or None
        numero_edicion = request.POST.get("numero_edicion") or None
        duracion = request.POST.get("duracion")
        director = request.POST.get("director") or None
        disponible = True
        
        # Convertir campos numéricos vacíos a None
        if numero_paginas == "":
            numero_paginas = None
        elif numero_paginas is not None:
            numero_paginas = int(numero_paginas)
            
        if duracion == "":
            duracion = None
        elif duracion is not None:
            duracion = int(duracion)
        
        nuevo_material = Material(
            codigo_inventario=codigo_inventario,
            titulo=titulo,
            tipo=tipo,
            autor=autor,
            isbn=isbn,
            numero_paginas=numero_paginas,
            fecha_publicacion=fecha_publicacion,
            numero_edicion=numero_edicion,
            duracion=duracion,
            director=director,
            disponible=disponible
        )
        nuevo_material.save()
        return redirect('lista_materiales')
    else:
        return render(request, "agregar_material.html")

def lista_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, "listados/lista_prestamos.html", {"prestamos": prestamos})


def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "listados/lista_usuarios.html", {"usuarios": usuarios})

def lista_materiales(request):
    materiales = Material.objects.all()
    return render(request, "listados/lista_materiales.html", {"materiales": materiales})

def adios(request):
    return HttpResponse(b"Adios")

def devuelve_fecha(request):
    fecha_actual = date.today()
    mensaje = f"Hoy es {fecha_actual}"
    return render(request, "base.html", {"mensaje": mensaje})

