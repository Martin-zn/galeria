from django.db import models
from django.conf import settings


# Create your models here.
class Obras(models.Model):
    id_obra              = models.AutoField(db_column='idObra', primary_key=True) 
    nombre           = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    imgUrl = models.CharField(max_length=500, default='https://img.freepik.com/foto-gratis/paleta-colores-sucios-tubos-acuarela_23-2148662999.jpg?t=st=1720018054~exp=1720021654~hmac=4279a3e9f9ffcff619ad6a5131bc6ae5dc3b5f071f3e237e1c1b2f1406a32c64&w=996')
    fecha_creacion = models.DateField(blank=False, null=False) 
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'obras')  

    def __str__(self):
        return str(self.nombre)
    
 