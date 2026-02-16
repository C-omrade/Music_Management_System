from .models import Song
from .serializers import SongSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser,IsAuthenticated
# Song properties
# List all songs
# List all songs according to mood
# list all songs according to genre
# Sort and searching options within the song

class SongsListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    # queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get_queryset(self):
        queryset = Song.objects.all()
        mood = self.request.query_params.get('mood')
        genre = self.request.query_params.get('genre')
        
        if(mood):
            queryset = queryset.filter(mood__icontains=mood)
    
        if(genre):
            queryset = queryset.filter(genre__icontains=genre)
        return queryset


# Add a new song with most of the details available coming from frontend
# Update a particular song details (due to change in Model or something else)
