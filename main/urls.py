
from django.urls import path

from . import views
urlpatterns = [
    path('vendors/',views.VendorList.as_view(),name='vendor-list' ),
    path('vendor/<int:pk>/',views.VendorDetail.as_view(),name='vendor-detail' ),
    path('products/',views.ProductList.as_view(),name='product-list' ),
    path('product/<slug:slug>/',views.ProductDetail.as_view(),name='product-detail' ),
]
