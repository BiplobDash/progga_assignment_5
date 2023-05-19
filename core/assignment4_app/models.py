from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Tags(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    img = models.ImageField(upload_to="products")
    name = models.CharField(max_length=30)
    tags = models.ManyToManyField(Tags)
    category = models.ManyToManyField(Category)
    description = models.TextField(max_length=100)
    
