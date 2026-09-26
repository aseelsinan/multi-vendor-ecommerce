from rest_framework import serializers
from . import models




# ----------------------------
# Vendor Serialzers
# ----------------------------
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['id', 'user', 'address']
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = {
            "id": instance.user.id,
            "username": instance.user.username,
            "email": instance.user.email
        }
        return response



# ----------------------------
# Product Serialzers
# ----------------------------

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Product
        fields=['id','vendor','category','title','slug','detail','price']

    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['vendor']={
            'user':instance.vendor.user.username
        }
        response['category']={
            'title':instance.category.title
        }
        
        return response