from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.
class Products(models.Model): 
    name= models.CharField(max_length=255, null=False)
    description= models.TextField()
    price= models.DecimalField(default=0, max_digits=6, decimal_places=2)
    photo = models.ImageField(null=True, upload_to = 'products/')
    category = models.ForeignKey('Category', null=True ,on_delete=models.CASCADE)

class Category(models.Model):
    name= models.CharField(max_length=255, null=False) 