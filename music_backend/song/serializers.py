from rest_framework import serializers
from .models import Song
from singer.serializers import SingerSerializer
from movies.serializers import MovieSerializer


class SongSerializer(serializers.ModelSerializer):
    singer = SingerSerializer()
    movie = MovieSerializer()
    class Meta:
        model = Song
        fields = ('name','length','mood','genre','lyrics','singer','movie')

