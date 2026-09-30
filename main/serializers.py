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
# Product Rating And Reviews
# ----------------------------
class ProductReviewSerialzier(serializers.ModelSerializer):

    class Meta:
        model=models.ProductRating
        fields=['rating', 'reviews','created_at']
    def to_representation(self, instance):
        repsonse= super().to_representation(instance)
        repsonse['customer']={
            'user':instance.customer.user.username
        }
        repsonse['product']={
            'product':instance.product.title
        }
        return repsonse

# ----------------------------
# Product Serialzers
# ----------------------------

# Product Category
class ProductCategorySerializer(serializers.ModelSerializer):
    total_products = serializers.IntegerField(read_only=True)
    class Meta:
        model=models.ProductCategory
        fields=['id','title','slug','icon','detail','total_products']

# Product
class ProductSerializer(serializers.ModelSerializer):
    product_rating=ProductReviewSerialzier(many=True )
    class Meta:
        model=models.Product
        fields=['id','vendor','category','title','slug','detail','price','product_rating']

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
        response= super().to_representation(instance)
        response['user']={
            'username':instance.user.username
        }
        return response



class CustomerAdreesSerializer(serializers.ModelSerializer):
      class Meta:
            model=models.CustomerAdrees
            fields=['customer','address','is_default']
      def to_representation(self, instance):
            response= super().to_representation(instance)
            response['customer']={
                'username':instance.customer.user.username
            }
            return response

# ----------------------------
# Order Serializers
# ----------------------------


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.OrderItem
        fields=['id','order','product']

    def to_representation(self,instance):
        response=super().to_representation(instance)
        response['order_items']=instance.order.id
        response['product']={
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

