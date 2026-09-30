from django.db.models import Count
from rest_framework import generics,viewsets
from . import serializers
from . import models


# ----------------------------
# Vendor Views
# ----------------------------
class VendorList(generics.ListCreateAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class=serializers.VendorSerializer

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class=serializers.VendorSerializer


    
# ----------------------------
# Product Views
# ----------------------------

class ProducCategorytList(generics.ListCreateAPIView):
    queryset=models.ProductCategory.objects.all()
    queryset = models.ProductCategory.objects.annotate(
        total_products=Count('product_category')  
    )
    serializer_class=serializers.ProductCategorySerializer
class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.ProductCategory.objects.all()
    serializer_class=serializers.ProductCategorySerializer
    lookup_field='slug'


class ProductList(generics.ListCreateAPIView):
    queryset=models.Product.objects.all()
    serializer_class=serializers.ProductSerializer
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Product.objects.all()
    serializer_class=serializers.ProductSerializer




# ----------------------------
# Customer views
# ----------------------------

class CustomerList(generics.ListCreateAPIView):
    queryset=models.Customer.objects.all()
    serializer_class=serializers.CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Customer.objects.all()
    serializer_class=serializers.CustomerSerializer


class CustomerAddressViewset(viewsets.ModelViewSet):
    queryset=models.CustomerAdrees.objects.all()
    serializer_class=serializers.CustomerAdreesSerializer

# ----------------------------
# Product views
# ----------------------------

class OrderList(generics.ListCreateAPIView):
    queryset=models.Order.objects.all()
    serializer_class=serializers.OrderSerailizer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = models.Order.objects.all()
   serializer_class = serializers.OrderSerailizer

# ----------------------------
# Product Rating views
# ----------------------------
class ProductRatingViewset(viewsets.ModelViewSet):
    queryset=models.ProductRating.objects.all()
    serializer_class=serializers.ProductReviewSerialzier