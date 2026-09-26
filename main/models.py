from django.db import models
from django.contrib.auth.models import User


# Vendor Model
class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address=models.TextField(null=True)

    def __str__(self):
        return f'{self.user.username}'
    
# Products

class ProductCategory(models.Model):
    title=models.CharField(max_length=200)
    detail=models.TextField(null=True)

    def __str__(self):
        return f'{self.title}'



class Product(models.Model):
    title=models.CharField(max_length=200)
    detail=models.TextField(null=True)
    price=models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.title}'


