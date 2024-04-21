from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()