from rest_framework import generics,permissions
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




# ----------------------------
# Product views
# ----------------------------

class OrderList(generics.ListCreateAPIView):
    queryset=models.Order.objects.all()
    serializer_class=serializers.OrderSerailizer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Order.objects.all()
    serializer_class=serializers.OrderItemsSerializer

    