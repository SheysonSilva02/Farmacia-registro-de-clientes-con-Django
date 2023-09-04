from django.shortcuts import render, redirect
from .models import Cliente
from django.contrib import messages

# Create your views here.
def home(request):
    listaClientes = Cliente.objects.all()
    #messages.success(request, '¡Clientes listados!')
    return render(request, "gestionClientes.html", {"clientes":listaClientes})

def registrarCliente(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    telefono=request.POST['txtTelefono']

    cliente = Cliente.objects.create(codigo=codigo, nombre=nombre,apellido=apellido,telefono=telefono)
    messages.success(request, '¡Cliente registrado!')

    return redirect('/')

def edicionCliente(request, codigo):
    cliente = Cliente.objects.get(codigo=codigo)
    return render(request, "edicionCliente.html", {"cliente": cliente})

def editarCliente(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    telefono=request.POST['txtTelefono']

    cliente = Cliente.objects.get(codigo=codigo)
    cliente.nombre=nombre
    cliente.apellido=apellido
    cliente.telefono=telefono
    cliente.save()

    messages.success(request, '¡Cliente actualizado!')

    return redirect('/')


def eliminarCliente(request, codigo):
    cliente = Cliente.objects.get(codigo=codigo)
    cliente.delete()

    messages.success(request, '¡Cliente eliminado!')

    return redirect('/')