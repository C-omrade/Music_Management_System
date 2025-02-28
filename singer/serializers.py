from rest_framework import serializers
from .models import Singer

# name, age, followers, image
# no other serializer needed
class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = "__all__"
