import datetime
from django.http import HttpResponse
from django.shortcuts import render

from aplicacion.models import Artista, Obras

# Create your views here.

def categoriaEdad(request, edad):
    if edad >= 18:
        if edad >= 60:
            descripcion = "Viejo culiao"
        else: 
            descripcion = "Esta bien"
    else:
        descripcion = "Pendejo culiao"
    resultado = "<h1>Categoria etaria: %s</h1>" %descripcion

    return HttpResponse(resultado)

def reloj(request):
    respuesta = "<h1>Hora actual: {0}</h1>".format(datetime.datetime.now())
    return HttpResponse(respuesta)

def firstIndex(request):

    favoriteNumbers = [1,2,3,4,5]

    context={'mensaje': "Esto esta funcionando", 'favoriteNumbers':favoriteNumbers}
    return render(request, 'index.html', context)


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

def obras_view(request):
    obras = Obras.objects.all()
    context = {'obras':obras}
    return render(request, 'obras.html', context)

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

