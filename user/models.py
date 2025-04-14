from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) #stores when user was created
    city = models.CharField(max_length=100,blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    phone_no = models.CharField(max_length=15,blank=True,null=True)
    subscription = models.BooleanField(default=0) # 0 for normal User
    
    def __str__(self):
        return self.name