from django.db import transaction

from .models import Album, Track


@transaction.atomic
def cargar_datos_ejemplo():
    if Album.objects.exists():
        return

    album = Album.objects.create(titulo="Abbey Road", artista="The Beatles")
    Track.objects.create(album=album, titulo="Come Together", duracion_seg=259)
    Track.objects.create(album=album, titulo="Something", duracion_seg=182)
