# Generated by Django 5.0.6 on 2024-07-03 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_artista_imgurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='artista',
            name='descripcion',
            field=models.CharField(default='sin descripcion', max_length=255),
        ),
    ]