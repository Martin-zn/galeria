from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Obras

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'imgUrl', 'descripcion', 'telefono', 'location']

class ObraForm(forms.ModelForm):
    class Meta:
        model = Obras
        fields = ['nombre', 'descripcion', 'imgUrl', 'fecha_creacion']
        widgets = {
            'fecha_creacion': forms.DateInput(attrs={'type': 'date'}),
        }