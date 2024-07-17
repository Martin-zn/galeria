from itertools import count
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from aplicacion.Carrito import Carrito
from aplicacion.models import Obras
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.db.models import Count
from .forms import ObraForm


# Create your views here.


def exit(request):
    logout(request)
    return redirect('/galeria/home')

def home(request):
    ultimasObras = Obras.objects.order_by('-id_obra')[:3]
    obras = Obras.objects.order_by('-id_obra')[:5]
    
    User = get_user_model()
    usuarios = User.objects.filter(is_active=True).order_by('id')[:5]

    usuarios_data = []
    for usuario in usuarios:
        usuarios_data.append({
            'id': usuario.id,
            'nombre': f"{usuario.first_name} {usuario.last_name}",
            'descripcion': usuario.descripcion,
            'imgUrl': usuario.imgUrl,
            'cantidad_obras': usuario.obras.count()
        })

    context = {
        'ultimasObras': ultimasObras,
        'usuarios': usuarios_data,
        'obras': obras
    }
    return render(request, 'home.html', context)


@login_required
def obras_view(request):
    query = request.GET.get('q')
    if query:
        obras = Obras.objects.filter(nombre__icontains=query) | Obras.objects.filter(usuario__username__icontains=query)
    else:
        obras = Obras.objects.all()
    context = {'obras': obras, 'query': query}
    return render(request, 'obras.html', context)

@login_required
def artistas_view(request):
    query = request.GET.get('q')
    User = get_user_model()

    if query:
        usuarios = User.objects.filter(is_active=True).filter(
            first_name__icontains=query
        ) | User.objects.filter(
            last_name__icontains=query
        ).annotate(
            cantidad_obras=Count('obras')
        ).order_by('id')
    else:
        usuarios = User.objects.filter(is_active=True).annotate(
            cantidad_obras=Count('obras')
        ).order_by('id')

    usuarios_data = []
    for usuario in usuarios:
        usuarios_data.append({
            'id': usuario.id,
            'nombre': f"{usuario.first_name} {usuario.last_name}",
            'descripcion': usuario.descripcion,
            'imgUrl': usuario.imgUrl,
            'cantidad_obras': usuario.obras.count()
        })

    context = {'artistas': usuarios_data, 'query': query}
    return render(request, 'artistas.html', context)



@login_required
def obra_page(request, nombre):
    obra = get_object_or_404(Obras, nombre=nombre)
    context = {'obra': obra}
    return render(request, 'obraPage.html', context)

@login_required
def artista_page(request, id):
    User = get_user_model()
    usuario = get_object_or_404(User, id=id)
    obras = usuario.obras.all()  
    context = {'artista': usuario, 'obras': obras}
    return render(request, 'artistaPage.html', context)

@login_required
def user_page(request):
    if request.method == 'POST':
        form = ObraForm(request.POST)
        if form.is_valid():
            obra = form.save(commit=False)
            obra.usuario = request.user
            obra.save()
            return redirect('user')
    else:
        form = ObraForm()
    
    obras = Obras.objects.filter(usuario=request.user)
    context = {
        'user': request.user,
        'form': form,
        'obras': obras
    }
    return render(request, 'usuario.html', context)
   


def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(request, username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])

            login(request, user)

            return redirect('home')


    return render(request, 'registration/register.html', data)


# Metodos para el carrito

def agregar_obra(request, obra_id):
    carrito = Carrito(request)
    obra = get_object_or_404(Obras, id_obra=obra_id)
    carrito.agregar(obra)
    return redirect('carrito')

def eliminar_obra(request, obra_id):
    carrito = Carrito(request)
    obra = get_object_or_404(Obras, id_obra=obra_id)
    carrito.eliminar(obra)
    return redirect('carrito')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('carrito')

@login_required
def carrito(request):
    return render(request, 'carrito.html')



