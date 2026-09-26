from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField




# ----------------------------
# Vendor
# ----------------------------
class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address=models.TextField(null=True)

    def __str__(self):
        return f'{self.user.username}'
    


# ----------------------------
# Product 
# ----------------------------
class ProductCategory(models.Model):
    title=models.CharField(max_length=200)
    detail=models.TextField(null=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
          verbose_name_plural=' Product Categories'
    


class Product(models.Model):
    vendor=models.ForeignKey(Vendor, related_name='product', on_delete=models.CASCADE)
    category=models.ForeignKey(ProductCategory, related_name='product_category',null=True, on_delete=models.SET_NULL)
    title=models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True, always_update=False)
    detail=models.TextField(null=True,blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.title}'


