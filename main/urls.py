
from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('customer-adress',views.CustomerAddressViewset)
router.register('product-rating',views.ProductRatingViewset)
urlpatterns = [
    # Vendors
    path('vendors/',views.VendorList.as_view(),name='vendor-list' ),
    path('vendor/<int:pk>/',views.VendorDetail.as_view(),name='vendor-detail' ),
   
   
    # Categories
    path('categories/',views.ProducCategorytList.as_view(),name='categories-list' ),
    path('category/<slug:slug>/',views.ProductCategoryDetail.as_view(),name='category-deatail' ),
    
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

urlpatterns += router.urls

