import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from aplicacion.models import Artista, Obras

# Create your views here.


def exit(request):
    logout(request)
    return redirect('/galeria/home')

def home(request):
    ultimasObras = Obras.objects.order_by('id_obra')[:3]
    obras = Obras.objects.order_by('id_obra')[:5]
    mensaje = 'CHAMA'
    
    artistas = Artista.objects.order_by('id_artista')[:5].prefetch_related('obras_set')

    artistas_data = []
    for artista in artistas:
        artistas_data.append({
            'id': artista.id_artista,
            'nombre': artista.nombre,
            'descripcion': artista.descripcion,
            'imgUrl': artista.imgUrl,
            'cantidad_obras': artista.obras_set.count()
        })

    context={'mensaje': mensaje, 'ultimasObras':ultimasObras, 'artistas':artistas_data, 'obras':obras}
    return render(request, 'home.html', context)


@login_required
def obras_view(request):
    obras = Obras.objects.all()
    context = {'obras':obras}
    return render(request, 'obras.html', context)
@login_required
def artistas_view(request):
    obras = Obras.objects.all()
    artistas = Artista.objects.order_by('id_artista').all().prefetch_related('obras_set')
    artistas_data = []
    for artista in artistas:
        artistas_data.append({
            'id': artista.id_artista,
            'nombre': artista.nombre,
            'descripcion': artista.descripcion,
            'imgUrl': artista.imgUrl,
            'cantidad_obras': artista.obras_set.count()
        })

    context={'artistas':artistas_data}
    return render(request, 'artistas.html', context)
@login_required
def obra_page(request, nombre):
    obra = get_object_or_404(Obras, nombre=nombre)
    context = {'obra': obra}
    return render(request, 'obraPage.html', context)

@login_required
def artista_page(request, nombre):
    artista = Artista.objects.get(nombre=nombre)
    obras = Obras.objects.filter(id_artista=artista)
    context = {'artista': artista, 'obras': obras}
    return render(request, 'artistaPage.html', context)






