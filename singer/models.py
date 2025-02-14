from django.db import models

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=100,null=True,blank=False)
    age = models.IntegerField(default=20,blank=False,null=False)
    followers = models.IntegerField(default=0)
    image = models.ImageField(blank=True,null=True)
    def __str__(self):
        return self.name+" -> On the beat"