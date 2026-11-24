from rest_framework import serializers

from .models import Album, Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)  # muestra las canciones dentro del álbum

    class Meta:
        model = Album
        fields = ["id", "titulo", "artista", "tracks"]
