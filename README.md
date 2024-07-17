# Galería de Arte Online

Este proyecto es una galería de arte online desarrollada con Django y Bootstrap, que permite a los usuarios ver y comprar obras de arte. La galería incluye una página de inicio, una página de obras de arte, una página de artistas y un carrito de compras. La base de datos utilizada es SQLite3.

## Caracteristicas

Página de inicio: Introducción a la galería con información destacada.
Página de obras de arte: Visualización de las obras disponibles con detalles como nombre, descripción, imagen y fecha de creación.
Página de artistas: Información sobre los artistas, incluyendo sus obras y perfiles.
Carrito de compras: Funcionalidad para agregar obras al carrito y proceder con la compra.

## Requisitos

 - [Python 3.xs](https://www.python.org/)
 - [Django](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/)
 - [Bootstrap](https://getbootstrap.com/)
 - SQLite

## Instalacion

Clonar Repositorio
```bash
  git clone https://github.com/tuusuario/galeria-arte.git
cd galeria-arte
```

Crear y activar un entorno virtual:
```bash
  python -m venv env
source env/bin/activate  # En Windows usa: env\Scripts\activate
```

Instalar las dependencias:
```bash
  pip install -r requirements.txt
```

Ejecutar el servidor de desarrollo:
```bash
  python manage.py runserver
```
