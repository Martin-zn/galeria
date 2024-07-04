from django.db import models

# Create your models here.

class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)

class Artista(models.Model):
    id_artista       = models.AutoField(db_column='idArtista', primary_key=True) 
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    id_genero        = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')  
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  
    imgUrl           = models.CharField(max_length=255, default='https://img.freepik.com/foto-gratis/paleta-colores-sucios-tubos-acuarela_23-2148662999.jpg?t=st=1720018054~exp=1720021654~hmac=4279a3e9f9ffcff619ad6a5131bc6ae5dc3b5f071f3e237e1c1b2f1406a32c64&w=996')
    descripcion          = models.CharField(max_length=255, default='sin descripcion')
    activo           = models.IntegerField()


    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)  

class Obras(models.Model):
    id_obra              = models.AutoField(db_column='idObra', primary_key=True) 
    nombre           = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    imgUrl = models.CharField(max_length=255, default='https://img.freepik.com/foto-gratis/paleta-colores-sucios-tubos-acuarela_23-2148662999.jpg?t=st=1720018054~exp=1720021654~hmac=4279a3e9f9ffcff619ad6a5131bc6ae5dc3b5f071f3e237e1c1b2f1406a32c64&w=996')
    id_artista = models.ForeignKey('Artista',on_delete=models.CASCADE, db_column='idArtista')  
    fecha_creacion = models.DateField(blank=False, null=False) 

    def __str__(self):
        return str(self.nombre)
    
 