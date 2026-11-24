from django.db import models


class Album(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class Track(models.Model):
    # Si se borra el álbum, se borran sus canciones (cascada)
    album = models.ForeignKey(Album, related_name="tracks", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    duracion_seg = models.IntegerField(default=180)

    def __str__(self):
        return self.titulo
