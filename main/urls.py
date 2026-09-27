
from django.urls import path

from . import views
urlpatterns = [
    # Vendors
    path('vendors/',views.VendorList.as_view(),name='vendor-list' ),
    path('vendor/<int:pk>/',views.VendorDetail.as_view(),name='vendor-detail' ),
   
    # Products
   
    path('products/',views.ProductList.as_view(),name='product-list' ),
    path('product/<slug:slug>/',views.ProductDetail.as_view(),name='product-detail' ),
   
    # Customers
   
    path('customers/',views.CustomerList.as_view(),name='customers-list' ),
    path('customer/<int:pk>',views.CustomerDetail.as_view(),name='customers-detail' ),

    # orders
   
    path('orders/',views.OrderList.as_view(),name='order-list' ),
    path('order/<int:pk>',views.OrderDetail.as_view(),name='order-detail' ),
]
