from django.contrib import admin

from aplicacion.models import Artista, Genero, Obras

# Register your models here.

admin.site.register(Genero)
admin.site.register(Artista)
admin.site.register(Obras)