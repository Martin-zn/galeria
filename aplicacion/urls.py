from . import views
from django.urls import include, path



urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', views.home, name='home'),
    path('obras/', views.obras_view, name='obras'),
    path('artistas/', views.artistas_view, name='artistas'),
    path('obra/<str:nombre>/', views.obra_page, name='obra_page'),
    path('artista/<int:id>/', views.artista_page, name='artista_page'),
    path('logout/', views.exit, name='exit'),
    path('usuario/', views.user_page, name='user'),
    path('register/', views.register, name='register'),

]