from rest_framework import serializers
from .models import Movie

# no foreign field
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"