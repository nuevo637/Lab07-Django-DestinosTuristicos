from django.db import models

class DestinosTuristicos(models.Model):
    nombreCiudad = models.CharField(max_length = 100)
    imagenCiudad = models.ImageField(upload_to = 'pics')
    descripcionCiudad = models.TextField()
    precioTour = models.IntegerField()
    ofertaTour = models.BooleanField(default=False)