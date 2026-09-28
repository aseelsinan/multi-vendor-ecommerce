from django.contrib import admin
from . import models



# ----------------------------
# Vendor 
# ----------------------------

@admin.register(models.Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'address']
    search_fields = ['user__username', 'address']

# ----------------------------
# Products
# ----------------------------
admin.site.register(models.ProductCategory)

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['title', 'detail', 'price']
  search_fields = ['title']


# ----------------------------
# Customers
# ----------------------------
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
   search_fields=['user__username']

# ----------------------------
# Orders
# ----------------------------

admin.site.register(models.Order)
admin.site.register(models.OrderItem)