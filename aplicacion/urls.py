from . import views
from django.urls import path


urlpatterns = [
    path('firstindex/', views.firstIndex),
    path('home/', views.home, name='home'),
    path('obras/', views.obras_view, name='obras'),
    path('artistas/', views.artistas_view, name='artistas'),
    path('obra/<str:nombre>/', views.obra_page, name='obra_page'),
    path('artista/<str:nombre>/', views.artista_page, name='artista_page'),
]