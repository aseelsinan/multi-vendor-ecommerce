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
            "username": instance.user.username,
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



# ----------------------------
# Customer Serializer
# ----------------------------
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Customer
        fields=['user','mobile_number']
    def to_representation(self, instance):
        resonse= super().to_representation(instance)
        resonse['user']={
            'username':instance.user.username
        }
        return resonse






# ----------------------------
# Order Serializers
# ----------------------------


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.OrderItem
        fields=['id','order','product']

    def to_representation(self,instance):
        response=super.to_representation(instance)
        response['oreder']=instance.order.id
        response['product']={
            'id':instance.product.id,
            'title':instance.product.title,
            'price':instance.product.price,
            }
        return response



class OrderSerailizer(serializers.ModelSerializer):
    order_items = OrderItemsSerializer(many=True, read_only=True)
    class Meta:
        model=models.Order
        fields=['id','customer','order_at','order_items']

    def to_representation(self, instance):
        response= super().to_representation(instance)
        response['customer']={
            'username':instance.customer.user.username
        }
        return response

