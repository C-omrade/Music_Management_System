from django.db import models

# Create your models here.
movie_type = [
    ('hollywood','Hollywood'),
    ('bollywood','Bollywood'),
    ('tollywood','Tollywood'),
    ('punjabi','Punjabi')
]
class Movie(models.Model):
    name = models.CharField(max_length=100,blank=False,null=True)
    type = models.CharField(max_length=100,choices=movie_type,default='bollywood')
    cast = models.TextField(default="Tell use the actors and acctresses")
    length = models.DecimalField(decimal_places=2,max_digits=5,null=True)
    release_date = models.DateTimeField(null=True)
    description = models.TextField(default="Tell us something about movies")
    