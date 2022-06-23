from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length = 200)
    biography = models.TextField(max_length = 2000)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    country = models.CharField(max_length = 200)
    image = models.ImageField(upload_to="artists", null= True,  height_field=None, width_field=None, max_length=100)
    
class Meduim(models.Model):
    description = models.CharField(max_length=200)
    status = models.BooleanField()
    
class Museum(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(max_length=2000)
    city = models.CharField(max_length = 250)
    country = models.CharField(max_length = 250)
    address = models.CharField(max_length = 500)
    lat = models.FloatField()
    lon = models.FloatField()
    image = models.ImageField(upload_to="museums", null=True, height_field=None, width_field=None, max_length=100)
    
class CulturalProperty(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(max_length=2000)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)       
    medium = models.ForeignKey(Meduim, on_delete=models.CASCADE)       
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE)       
    image = models.ImageField(upload_to="museums", null=True, height_field=None, width_field=None, max_length=100)
    
            
    
    