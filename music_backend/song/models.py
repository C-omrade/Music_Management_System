from django.db import models
from singer.models import Singer
from movies.models import Movie

mood_choices = [
    ('sad','Sad'),
    ('romantic','Romantic'),
    ('love','Love'),
    ('fun','Fun'),
    ('happy','Happy'),
    ('motivational','Motivational'),
    ('heartbreak','Heartbreak'),
]
genre_choices = [
    ('rock','Rock'),
    ('pop','Pop'),
    ('hip-hop','Hip-Hop'),
    ('blues','Blues'),
]
class Song(models.Model):
    name = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer,on_delete=models.CASCADE)# This will be a foreign key to singer model in singer app 
    movie = models.ForeignKey(Movie,on_delete=models.DO_NOTHING) # This will be a foreign key to the movie model app 
    length = models.DecimalField(decimal_places=2,max_digits=5)
    mood = models.CharField(max_length=20,choices=mood_choices,default='happy')
    genre = models.CharField(max_length=20,choices=genre_choices,default='pop')
    lyrics = models.TextField(default="Lyrics are not available")
    def __str__(self):
        return "** "+self.name+" **"
