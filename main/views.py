from rest_framework import generics,permissions
from . import serializers
from . import models


#Vendor Operations 
class VendorList(generics.ListCreateAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class=serializers.VendorSerialezer

class VendorDetail(generics.RetrieveAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class=serializers.VendorSerializer
    