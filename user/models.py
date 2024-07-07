from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    imgUrl = models.CharField(max_length=255, default='https://w7.pngwing.com/pngs/178/595/png-transparent-user-profile-computer-icons-login-user-avatars-thumbnail.png')
    location = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.CharField(max_length=500 )
    telefono         = models.CharField(max_length=45)